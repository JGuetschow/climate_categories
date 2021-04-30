"""Run this via `make climate_categories/data/CRF.yaml` in the main directory."""
import datetime
import pathlib

import natsort
import numpy as np
import treelib
from unfccc_di_api import UNFCCCApiReader

import climate_categories

OUTPATH = pathlib.Path("./climate_categories/data/CRFDI.yaml")

# there are some categories with different IDs, but the same code and title.
# These are the categories directly under the top-level totals (e.g. 1. Energy),
# which are included in the category hierarchy once under the Total with and once
# under the Total without LULUCF.
#
# they can be safely merged because they are not actually different.


def parse_categories(r):
    used_categories = np.unique(r.annex_one_reader.variables["categoryId"])
    categories = {}
    for category_id in used_categories:
        try:
            raw_category = r.annex_one_reader.category_tree.nodes[category_id].tag
        except KeyError:
            if category_id == 10502:
                raw_category = "Total land area"
            elif category_id == 10503:
                raw_category = "GDP"
            elif category_id == 10504:
                raw_category = "Total population"
            else:
                raw_category = f"{category_id} Unknown category no. {category_id}"

        if raw_category[0].isnumeric():
            code, title = raw_category.split(maxsplit=1)
            if code.endswith("."):
                altcodes = [code, str(category_id)]
                code = code[:-1]
            else:
                altcodes = [str(category_id)]
        else:
            code = str(category_id)
            title = raw_category
            altcodes = []

        if code == "1.AA":
            altcodes += ["1.A", "1A", "1 A"]

        if code not in categories:
            categories[code] = {"title": title}

        altcode = code.replace(".", "")
        if altcode != code:
            altcodes.append(altcode)
            altcodes.append(code.replace(".", " "))

        if altcodes:
            if "alternative_codes" not in categories[code]:
                categories[code]["alternative_codes"] = []
            for ac in altcodes:
                if ac not in categories[code]["alternative_codes"]:
                    categories[code]["alternative_codes"].append(ac)

        if "info" not in categories[code]:
            categories[code]["info"] = {}
        if "numerical_ids" not in categories[code]["info"]:
            categories[code]["info"]["numerical_ids"] = []
        categories[code]["info"]["numerical_ids"].append(int(category_id))

    return categories


def add_relationships(r, categories):
    for code in categories:
        child_codes = []
        for nid in categories[code]["info"]["numerical_ids"]:
            try:
                for child in r.annex_one_reader.category_tree.children(nid):
                    try:
                        child_code = [
                            xcode
                            for xcode, x in categories.items()
                            if child.identifier in x["info"]["numerical_ids"]
                        ][0]
                        child_codes.append(child_code)
                    except IndexError:  # child code is not used in the data, discard
                        continue
            except treelib.tree.NodeIDAbsentError:
                # parent code is not included in the metadata
                # can't guess children without metadata
                pass

        if child_codes:
            categories[code]["children"] = [child_codes]


def sort_categories(categories):
    sorted_categories = {}
    # start with "special" categories without a normal X.Y etc. numbering
    special = []
    normal = []
    for code in categories:
        if code.isnumeric() and int(code) > 10:
            special.append(code)
        else:
            normal.append(code)

    sorted_codes = sorted(special, key=int) + natsort.natsorted(normal)

    for cat in sorted_codes:
        sorted_categories[cat] = categories[cat]

    return sorted_categories


def main():
    r = UNFCCCApiReader()
    categories = parse_categories(r)
    add_relationships(r, categories)
    categories = sort_categories(categories)

    spec = {
        "name": "CRFDI",
        "title": "CRF GHG emission categories (DI query interface)",
        "comment": "Common Reporting Format categories of GHG emissions and removals "
        "and some other quantities as obtained from the di.unfccc.int flexible query "
        "interface",
        "references": "https://unfccc.int/process-and-meetings/"
        "transparency-and-reporting/greenhouse-gas-data/data-interface-help#eq-7",
        "institution": "UNFCCC",
        "last_update": datetime.date.today().isoformat(),
        "hierarchical": True,
        "total_sum": True,
        "categories": categories,
        "canonical_top_level_category": "8677",  # Total including LULUCF
    }

    CRFDI = climate_categories.HierarchicalCategorization.from_spec(spec)

    CRFDI.to_yaml(OUTPATH)

    climate_categories.HierarchicalCategorization.from_yaml(OUTPATH)


if __name__ == "__main__":
    main()
