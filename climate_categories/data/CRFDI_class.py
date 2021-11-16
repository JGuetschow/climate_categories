spec = {
    "name": "CRFDI_class",
    "title": "CRF GHG emission categories (DI query interface) + classifications",
    "comment": "Common Reporting Format categories of GHG emissions and removals and some other quantities as obtained from the di.unfccc.int flexible query interface extended by sub-classifications also provided by the DI flexible query interface",
    "references": "https://unfccc.int/process-and-meetings/transparency-and-reporting/greenhouse-gas-data/data-interface-help#eq-7",
    "institution": "UNFCCC",
    "hierarchical": True,
    "last_update": "2021-11-05",
    "total_sum": False,
    "canonical_top_level_category": "8677",
    "categories": {
        "8270": {
            "title": "CO₂ Emissions from Biomass",
            "info": {"numerical_ids": ["8270"]},
            "children": [["8270-1"]],
        },
        "8564": {
            "title": "International Bunkers",
            "alternative_codes": ["8564-10510"],
            "info": {"numerical_ids": ["8564"]},
            "children": [["10357", "8828"]],
        },
        "8677": {
            "title": "Total GHG emissions with LULUCF",
            "alternative_codes": ["8677-10510"],
            "info": {"numerical_ids": ["8677"]},
            "children": [["1", "2", "3", "4", "5", "6"]],
        },
        "8828": {
            "title": "International Navigation",
            "alternative_codes": ["8828-10510"],
            "info": {"numerical_ids": ["8828"]},
            "children": [
                ["8828-1", "8828-2", "8828-3", "8828-4", "8828-5", "8828-6", "8828-7"]
            ],
        },
        "8869": {
            "title": "Memo Items",
            "info": {"numerical_ids": ["8869"]},
            "children": [["8270", "8564", "8987"]],
        },
        "8987": {
            "title": "Multilateral Operations",
            "alternative_codes": ["8987-10510"],
            "info": {"numerical_ids": ["8987"]},
        },
        "10357": {
            "title": "International Aviation",
            "alternative_codes": ["10357-10510"],
            "info": {"numerical_ids": ["10357"]},
            "children": [["10357-1", "10357-2", "10357-3"]],
        },
        "10464": {
            "title": "Total GHG emissions without LULUCF",
            "alternative_codes": ["10464-10510"],
            "info": {"numerical_ids": ["10464"]},
            "children": [["1", "2", "3", "5", "6"]],
        },
        "10479": {
            "title": "Total GHG emissions without LULUCF including indirect CO₂",
            "alternative_codes": ["10479-10510"],
            "info": {"numerical_ids": ["10479"]},
        },
        "10480": {
            "title": "Total GHG emissions with LULUCF including indirect CO₂",
            "alternative_codes": ["10480-10510"],
            "info": {"numerical_ids": ["10480"]},
        },
        "10502": {
            "title": "Total land area",
            "alternative_codes": ["10502-10510"],
            "info": {"numerical_ids": ["10502"]},
        },
        "10503": {
            "title": "GDP",
            "alternative_codes": ["10503-10510"],
            "info": {"numerical_ids": ["10503"]},
        },
        "10504": {
            "title": "Total population",
            "alternative_codes": ["10504-10510"],
            "info": {"numerical_ids": ["10504"]},
        },
        "11022": {
            "title": "Memo Items",
            "info": {"numerical_ids": ["11022"]},
            "children": [["11023", "11024", "11025"]],
        },
        "11023": {
            "title": "Long-term Storage of C in Waste Disposal Sites",
            "alternative_codes": ["11023-10510"],
            "info": {"numerical_ids": ["11023"]},
        },
        "11024": {
            "title": "Annual Change in Total Long-term C Storage",
            "alternative_codes": ["11024-10510"],
            "info": {"numerical_ids": ["11024"]},
        },
        "11025": {
            "title": "Annual Change in Total Long-term C Storage in HWP Waste",
            "alternative_codes": ["11025-10510"],
            "info": {"numerical_ids": ["11025"]},
        },
        "11026": {
            "title": "Information Item",
            "info": {"numerical_ids": ["11026"]},
            "children": [["11027", "11028"]],
        },
        "11027": {
            "title": "Waste Incineration with Energy Recovery included as Biomass",
            "alternative_codes": ["11027-10510"],
            "info": {"numerical_ids": ["11027"]},
        },
        "11028": {
            "title": "Waste Incineration with Energy Recovery included as Fossil Fuels",
            "alternative_codes": ["11028-10510"],
            "info": {"numerical_ids": ["11028"]},
        },
        "11029": {
            "title": "Information Item",
            "info": {"numerical_ids": ["11029"]},
            "children": [["11030", "11031", "11032", "11033", "11034"]],
        },
        "11030": {
            "title": "Total Amount Captured for Storage",
            "alternative_codes": ["11030-10510"],
            "info": {"numerical_ids": ["11030"]},
        },
        "11031": {
            "title": "Total Amount of Imports for Storage",
            "alternative_codes": ["11031-10510"],
            "info": {"numerical_ids": ["11031"]},
        },
        "11032": {
            "title": "Total Amount of Exports for Storage",
            "alternative_codes": ["11032-10510"],
            "info": {"numerical_ids": ["11032"]},
        },
        "11033": {
            "title": "Total Amount of CO₂ Injected at Storage Sites",
            "alternative_codes": ["11033-10510"],
            "info": {"numerical_ids": ["11033"]},
        },
        "11034": {
            "title": "Total Leakage from Transport, Injection and Storage",
            "alternative_codes": ["11034-10510"],
            "info": {"numerical_ids": ["11034"]},
        },
        "11035": {
            "title": "Information Item",
            "info": {"numerical_ids": ["11035"]},
            "children": [["11036"]],
        },
        "11036": {
            "title": "HWP in SWDS",
            "alternative_codes": ["11036-10510"],
            "info": {"numerical_ids": ["11036"]},
        },
        "1": {
            "title": "Energy",
            "alternative_codes": [
                "1.",
                "10481",
                "8819",
                "1-10510",
                "10481-10510",
                "8819-10510",
            ],
            "info": {"numerical_ids": ["10481", "8819"]},
            "children": [["1.AA", "1.AB", "1.AD", "1.B", "1.C", "8869"]],
        },
        "1.A.1": {
            "title": "Energy Industries",
            "alternative_codes": [
                "10402",
                "1A1",
                "1 A 1",
                "1.A.1-10510",
                "10402-10510",
            ],
            "info": {"numerical_ids": ["10402"]},
            "children": [
                ["1.A.1.a", "1.A.1.b", "1.A.1.c"],
                ["1.A.1-1", "1.A.1-2", "1.A.1-3", "1.A.1-4", "1.A.1-5", "1.A.1-6"],
            ],
        },
        "1.A.1.a": {
            "title": "Public Electricity and Heat Production",
            "alternative_codes": [
                "9422",
                "1A1a",
                "1 A 1 a",
                "1.A.1.a-10510",
                "9422-10510",
            ],
            "info": {"numerical_ids": ["9422"]},
            "children": [
                ["1.A.1.a.i", "1.A.1.a.ii", "1.A.1.a.iii", "1.A.1.a.iv"],
                [
                    "1.A.1.a-1",
                    "1.A.1.a-2",
                    "1.A.1.a-3",
                    "1.A.1.a-4",
                    "1.A.1.a-5",
                    "1.A.1.a-6",
                ],
            ],
        },
        "1.A.1.a.i": {
            "title": "Electricity Generation",
            "alternative_codes": [
                "8616",
                "1A1ai",
                "1 A 1 a i",
                "1.A.1.a.i-10510",
                "8616-10510",
            ],
            "info": {"numerical_ids": ["8616"]},
            "children": [
                [
                    "1.A.1.a.i-1",
                    "1.A.1.a.i-2",
                    "1.A.1.a.i-3",
                    "1.A.1.a.i-4",
                    "1.A.1.a.i-5",
                    "1.A.1.a.i-6",
                ]
            ],
        },
        "1.A.1.a.ii": {
            "title": "Combined Heat and Power Generation",
            "alternative_codes": [
                "9614",
                "1A1aii",
                "1 A 1 a ii",
                "1.A.1.a.ii-10510",
                "9614-10510",
            ],
            "info": {"numerical_ids": ["9614"]},
            "children": [
                [
                    "1.A.1.a.ii-1",
                    "1.A.1.a.ii-2",
                    "1.A.1.a.ii-3",
                    "1.A.1.a.ii-4",
                    "1.A.1.a.ii-5",
                    "1.A.1.a.ii-6",
                ]
            ],
        },
        "1.A.1.a.iii": {
            "title": "Heat Plants",
            "alternative_codes": [
                "9971",
                "1A1aiii",
                "1 A 1 a iii",
                "1.A.1.a.iii-10510",
                "9971-10510",
            ],
            "info": {"numerical_ids": ["9971"]},
            "children": [
                [
                    "1.A.1.a.iii-1",
                    "1.A.1.a.iii-2",
                    "1.A.1.a.iii-3",
                    "1.A.1.a.iii-4",
                    "1.A.1.a.iii-5",
                    "1.A.1.a.iii-6",
                ]
            ],
        },
        "1.A.1.a.iv": {
            "title": "Other",
            "alternative_codes": [
                "8368",
                "1A1aiv",
                "1 A 1 a iv",
                "1.A.1.a.iv-10510",
                "8368-10510",
            ],
            "info": {"numerical_ids": ["8368"]},
            "children": [
                [
                    "1.A.1.a.iv-1",
                    "1.A.1.a.iv-2",
                    "1.A.1.a.iv-3",
                    "1.A.1.a.iv-4",
                    "1.A.1.a.iv-5",
                    "1.A.1.a.iv-6",
                ]
            ],
        },
        "1.A.1.b": {
            "title": "Petroleum Refining",
            "alternative_codes": [
                "9771",
                "1A1b",
                "1 A 1 b",
                "1.A.1.b-10510",
                "9771-10510",
            ],
            "info": {"numerical_ids": ["9771"]},
            "children": [
                [
                    "1.A.1.b-1",
                    "1.A.1.b-2",
                    "1.A.1.b-3",
                    "1.A.1.b-4",
                    "1.A.1.b-5",
                    "1.A.1.b-6",
                ]
            ],
        },
        "1.A.1.c": {
            "title": "Manufacture of Solid Fuels and Other Energy Industries",
            "alternative_codes": [
                "9004",
                "1A1c",
                "1 A 1 c",
                "1.A.1.c-10510",
                "9004-10510",
            ],
            "info": {"numerical_ids": ["9004"]},
            "children": [
                ["1.A.1.c.i", "1.A.1.c.ii", "1.A.1.c.iii", "1.A.1.c.iv"],
                [
                    "1.A.1.c-1",
                    "1.A.1.c-2",
                    "1.A.1.c-3",
                    "1.A.1.c-4",
                    "1.A.1.c-5",
                    "1.A.1.c-6",
                ],
            ],
        },
        "1.A.1.c.i": {
            "title": "Manufacture of Solid Fuels",
            "alternative_codes": [
                "10306",
                "1A1ci",
                "1 A 1 c i",
                "1.A.1.c.i-10510",
                "10306-10510",
            ],
            "info": {"numerical_ids": ["10306"]},
            "children": [
                [
                    "1.A.1.c.i-1",
                    "1.A.1.c.i-2",
                    "1.A.1.c.i-3",
                    "1.A.1.c.i-4",
                    "1.A.1.c.i-5",
                    "1.A.1.c.i-6",
                ]
            ],
        },
        "1.A.1.c.ii": {
            "title": "Oil and Gas Extraction",
            "alternative_codes": [
                "10425",
                "1A1cii",
                "1 A 1 c ii",
                "1.A.1.c.ii-10510",
                "10425-10510",
            ],
            "info": {"numerical_ids": ["10425"]},
            "children": [
                [
                    "1.A.1.c.ii-1",
                    "1.A.1.c.ii-2",
                    "1.A.1.c.ii-3",
                    "1.A.1.c.ii-4",
                    "1.A.1.c.ii-5",
                    "1.A.1.c.ii-6",
                ]
            ],
        },
        "1.A.1.c.iii": {
            "title": "Other Energy Industries",
            "alternative_codes": [
                "8335",
                "1A1ciii",
                "1 A 1 c iii",
                "1.A.1.c.iii-10510",
                "8335-10510",
            ],
            "info": {"numerical_ids": ["8335"]},
            "children": [
                [
                    "1.A.1.c.iii-1",
                    "1.A.1.c.iii-2",
                    "1.A.1.c.iii-3",
                    "1.A.1.c.iii-4",
                    "1.A.1.c.iii-5",
                    "1.A.1.c.iii-6",
                ]
            ],
        },
        "1.A.1.c.iv": {
            "title": "Other",
            "alternative_codes": [
                "8656",
                "1A1civ",
                "1 A 1 c iv",
                "1.A.1.c.iv-10510",
                "8656-10510",
            ],
            "info": {"numerical_ids": ["8656"]},
            "children": [
                [
                    "1.A.1.c.iv-1",
                    "1.A.1.c.iv-2",
                    "1.A.1.c.iv-3",
                    "1.A.1.c.iv-4",
                    "1.A.1.c.iv-5",
                    "1.A.1.c.iv-6",
                ]
            ],
        },
        "1.A.2": {
            "title": "Manufacturing Industries and Construction",
            "alternative_codes": ["8556", "1A2", "1 A 2", "1.A.2-10510", "8556-10510"],
            "info": {"numerical_ids": ["8556"]},
            "children": [
                [
                    "1.A.2.a",
                    "1.A.2.b",
                    "1.A.2.c",
                    "1.A.2.d",
                    "1.A.2.e",
                    "1.A.2.f",
                    "1.A.2.g",
                ],
                ["1.A.2-1", "1.A.2-2", "1.A.2-3", "1.A.2-4", "1.A.2-5", "1.A.2-6"],
            ],
        },
        "1.A.2.a": {
            "title": "Iron and Steel",
            "alternative_codes": [
                "10329",
                "1A2a",
                "1 A 2 a",
                "1.A.2.a-10510",
                "10329-10510",
            ],
            "info": {"numerical_ids": ["10329"]},
            "children": [
                [
                    "1.A.2.a-1",
                    "1.A.2.a-2",
                    "1.A.2.a-3",
                    "1.A.2.a-4",
                    "1.A.2.a-5",
                    "1.A.2.a-6",
                ]
            ],
        },
        "1.A.2.b": {
            "title": "Non-Ferrous Metals",
            "alternative_codes": [
                "9859",
                "1A2b",
                "1 A 2 b",
                "1.A.2.b-10510",
                "9859-10510",
            ],
            "info": {"numerical_ids": ["9859"]},
            "children": [
                [
                    "1.A.2.b-1",
                    "1.A.2.b-2",
                    "1.A.2.b-3",
                    "1.A.2.b-4",
                    "1.A.2.b-5",
                    "1.A.2.b-6",
                ]
            ],
        },
        "1.A.2.c": {
            "title": "Chemicals",
            "alternative_codes": [
                "9369",
                "1A2c",
                "1 A 2 c",
                "1.A.2.c-10510",
                "9369-10510",
            ],
            "info": {"numerical_ids": ["9369"]},
            "children": [
                [
                    "1.A.2.c-1",
                    "1.A.2.c-2",
                    "1.A.2.c-3",
                    "1.A.2.c-4",
                    "1.A.2.c-5",
                    "1.A.2.c-6",
                ]
            ],
        },
        "1.A.2.d": {
            "title": "Pulp, Paper and Print",
            "alternative_codes": [
                "10119",
                "1A2d",
                "1 A 2 d",
                "1.A.2.d-10510",
                "10119-10510",
            ],
            "info": {"numerical_ids": ["10119"]},
            "children": [
                [
                    "1.A.2.d-1",
                    "1.A.2.d-2",
                    "1.A.2.d-3",
                    "1.A.2.d-4",
                    "1.A.2.d-5",
                    "1.A.2.d-6",
                ]
            ],
        },
        "1.A.2.e": {
            "title": "Food Processing, Beverages and Tobacco",
            "alternative_codes": [
                "8321",
                "1A2e",
                "1 A 2 e",
                "1.A.2.e-10510",
                "8321-10510",
            ],
            "info": {"numerical_ids": ["8321"]},
            "children": [
                [
                    "1.A.2.e-1",
                    "1.A.2.e-2",
                    "1.A.2.e-3",
                    "1.A.2.e-4",
                    "1.A.2.e-5",
                    "1.A.2.e-6",
                ]
            ],
        },
        "1.A.2.f": {
            "title": "Non-metallic Minerals",
            "alternative_codes": [
                "8876",
                "1A2f",
                "1 A 2 f",
                "1.A.2.f-10510",
                "8876-10510",
            ],
            "info": {"numerical_ids": ["8876"]},
            "children": [
                [
                    "1.A.2.f-1",
                    "1.A.2.f-2",
                    "1.A.2.f-3",
                    "1.A.2.f-4",
                    "1.A.2.f-5",
                    "1.A.2.f-6",
                ]
            ],
        },
        "1.A.2.g": {
            "title": "Other",
            "alternative_codes": [
                "9832",
                "1A2g",
                "1 A 2 g",
                "1.A.2.g-10510",
                "9832-10510",
            ],
            "info": {"numerical_ids": ["9832"]},
            "children": [
                [
                    "1.A.2.g.i",
                    "1.A.2.g.ii",
                    "1.A.2.g.iii",
                    "1.A.2.g.iv",
                    "1.A.2.g.v",
                    "1.A.2.g.vi",
                    "1.A.2.g.vii",
                    "1.A.2.g.viii",
                ],
                [
                    "1.A.2.g-1",
                    "1.A.2.g-2",
                    "1.A.2.g-3",
                    "1.A.2.g-4",
                    "1.A.2.g-5",
                    "1.A.2.g-6",
                ],
            ],
        },
        "1.A.2.g.i": {
            "title": "Manufacturing of Machinery",
            "alternative_codes": [
                "10308",
                "1A2gi",
                "1 A 2 g i",
                "1.A.2.g.i-10510",
                "10308-10510",
            ],
            "info": {"numerical_ids": ["10308"]},
            "children": [
                [
                    "1.A.2.g.i-1",
                    "1.A.2.g.i-2",
                    "1.A.2.g.i-3",
                    "1.A.2.g.i-4",
                    "1.A.2.g.i-5",
                    "1.A.2.g.i-6",
                ]
            ],
        },
        "1.A.2.g.ii": {
            "title": "Manufacturing of Transport Equipment",
            "alternative_codes": [
                "10150",
                "1A2gii",
                "1 A 2 g ii",
                "1.A.2.g.ii-10510",
                "10150-10510",
            ],
            "info": {"numerical_ids": ["10150"]},
            "children": [
                [
                    "1.A.2.g.ii-1",
                    "1.A.2.g.ii-2",
                    "1.A.2.g.ii-3",
                    "1.A.2.g.ii-4",
                    "1.A.2.g.ii-5",
                    "1.A.2.g.ii-6",
                ]
            ],
        },
        "1.A.2.g.iii": {
            "title": "Mining (Excluding Fuels) and Quarrying",
            "alternative_codes": [
                "8527",
                "1A2giii",
                "1 A 2 g iii",
                "1.A.2.g.iii-10510",
                "8527-10510",
            ],
            "info": {"numerical_ids": ["8527"]},
            "children": [
                [
                    "1.A.2.g.iii-1",
                    "1.A.2.g.iii-2",
                    "1.A.2.g.iii-3",
                    "1.A.2.g.iii-4",
                    "1.A.2.g.iii-5",
                    "1.A.2.g.iii-6",
                ]
            ],
        },
        "1.A.2.g.iv": {
            "title": "Wood and Wood Products",
            "alternative_codes": [
                "8424",
                "1A2giv",
                "1 A 2 g iv",
                "1.A.2.g.iv-10510",
                "8424-10510",
            ],
            "info": {"numerical_ids": ["8424"]},
            "children": [
                [
                    "1.A.2.g.iv-1",
                    "1.A.2.g.iv-2",
                    "1.A.2.g.iv-3",
                    "1.A.2.g.iv-4",
                    "1.A.2.g.iv-5",
                    "1.A.2.g.iv-6",
                ]
            ],
        },
        "1.A.2.g.v": {
            "title": "Construction",
            "alternative_codes": [
                "10287",
                "1A2gv",
                "1 A 2 g v",
                "1.A.2.g.v-10510",
                "10287-10510",
            ],
            "info": {"numerical_ids": ["10287"]},
            "children": [
                [
                    "1.A.2.g.v-1",
                    "1.A.2.g.v-2",
                    "1.A.2.g.v-3",
                    "1.A.2.g.v-4",
                    "1.A.2.g.v-5",
                    "1.A.2.g.v-6",
                ]
            ],
        },
        "1.A.2.g.vi": {
            "title": "Textile and Leather",
            "alternative_codes": [
                "8721",
                "1A2gvi",
                "1 A 2 g vi",
                "1.A.2.g.vi-10510",
                "8721-10510",
            ],
            "info": {"numerical_ids": ["8721"]},
            "children": [
                [
                    "1.A.2.g.vi-1",
                    "1.A.2.g.vi-2",
                    "1.A.2.g.vi-3",
                    "1.A.2.g.vi-4",
                    "1.A.2.g.vi-5",
                    "1.A.2.g.vi-6",
                ]
            ],
        },
        "1.A.2.g.vii": {
            "title": "Off-road Vehicles and Other Machinery",
            "alternative_codes": [
                "8587",
                "1A2gvii",
                "1 A 2 g vii",
                "1.A.2.g.vii-10510",
                "8587-10510",
            ],
            "info": {"numerical_ids": ["8587"]},
            "children": [
                ["1.A.2.g.vii-1", "1.A.2.g.vii-2", "1.A.2.g.vii-3", "1.A.2.g.vii-4"]
            ],
        },
        "1.A.2.g.viii": {
            "title": "Other",
            "alternative_codes": [
                "8794",
                "1A2gviii",
                "1 A 2 g viii",
                "1.A.2.g.viii-10510",
                "8794-10510",
            ],
            "info": {"numerical_ids": ["8794"]},
            "children": [
                [
                    "1.A.2.g.viii-1",
                    "1.A.2.g.viii-2",
                    "1.A.2.g.viii-3",
                    "1.A.2.g.viii-4",
                    "1.A.2.g.viii-5",
                    "1.A.2.g.viii-6",
                ]
            ],
        },
        "1.A.3": {
            "title": "Transport",
            "alternative_codes": ["8322", "1A3", "1 A 3", "1.A.3-10510", "8322-10510"],
            "info": {"numerical_ids": ["8322"]},
            "children": [
                ["1.A.3.a", "1.A.3.b", "1.A.3.c", "1.A.3.d", "1.A.3.e"],
                ["1.A.3-1", "1.A.3-2", "1.A.3-3", "1.A.3-4", "1.A.3-5"],
            ],
        },
        "1.A.3.a": {
            "title": "Domestic Aviation",
            "alternative_codes": [
                "10419",
                "1A3a",
                "1 A 3 a",
                "1.A.3.a-10510",
                "10419-10510",
            ],
            "info": {"numerical_ids": ["10419"]},
            "children": [["1.A.3.a-1", "1.A.3.a-2", "1.A.3.a-3", "1.A.3.a-4"]],
        },
        "1.A.3.b": {
            "title": "Road Transportation",
            "alternative_codes": [
                "9607",
                "1A3b",
                "1 A 3 b",
                "1.A.3.b-10510",
                "9607-10510",
            ],
            "info": {"numerical_ids": ["9607"]},
            "children": [
                ["1.A.3.b.i", "1.A.3.b.ii", "1.A.3.b.iii", "1.A.3.b.iv", "1.A.3.b.v"],
                [
                    "1.A.3.b-1",
                    "1.A.3.b-2",
                    "1.A.3.b-3",
                    "1.A.3.b-4",
                    "1.A.3.b-5",
                    "1.A.3.b-6",
                    "1.A.3.b-7",
                    "1.A.3.b-8",
                ],
            ],
        },
        "1.A.3.b.i": {
            "title": "Cars",
            "alternative_codes": [
                "9279",
                "1A3bi",
                "1 A 3 b i",
                "1.A.3.b.i-10510",
                "9279-10510",
            ],
            "info": {"numerical_ids": ["9279"]},
            "children": [
                [
                    "1.A.3.b.i-1",
                    "1.A.3.b.i-2",
                    "1.A.3.b.i-3",
                    "1.A.3.b.i-4",
                    "1.A.3.b.i-5",
                    "1.A.3.b.i-6",
                    "1.A.3.b.i-7",
                    "1.A.3.b.i-8",
                ]
            ],
        },
        "1.A.3.b.ii": {
            "title": "Light Duty Trucks",
            "alternative_codes": [
                "9702",
                "1A3bii",
                "1 A 3 b ii",
                "1.A.3.b.ii-10510",
                "9702-10510",
            ],
            "info": {"numerical_ids": ["9702"]},
            "children": [
                [
                    "1.A.3.b.ii-1",
                    "1.A.3.b.ii-2",
                    "1.A.3.b.ii-3",
                    "1.A.3.b.ii-4",
                    "1.A.3.b.ii-5",
                    "1.A.3.b.ii-6",
                    "1.A.3.b.ii-7",
                    "1.A.3.b.ii-8",
                ]
            ],
        },
        "1.A.3.b.iii": {
            "title": "Heavy Duty Trucks and Buses",
            "alternative_codes": [
                "8358",
                "1A3biii",
                "1 A 3 b iii",
                "1.A.3.b.iii-10510",
                "8358-10510",
            ],
            "info": {"numerical_ids": ["8358"]},
            "children": [
                [
                    "1.A.3.b.iii-1",
                    "1.A.3.b.iii-2",
                    "1.A.3.b.iii-3",
                    "1.A.3.b.iii-4",
                    "1.A.3.b.iii-5",
                    "1.A.3.b.iii-6",
                    "1.A.3.b.iii-7",
                    "1.A.3.b.iii-8",
                ]
            ],
        },
        "1.A.3.b.iv": {
            "title": "Motorcycles",
            "alternative_codes": [
                "9622",
                "1A3biv",
                "1 A 3 b iv",
                "1.A.3.b.iv-10510",
                "9622-10510",
            ],
            "info": {"numerical_ids": ["9622"]},
            "children": [
                [
                    "1.A.3.b.iv-1",
                    "1.A.3.b.iv-2",
                    "1.A.3.b.iv-3",
                    "1.A.3.b.iv-4",
                    "1.A.3.b.iv-5",
                    "1.A.3.b.iv-6",
                    "1.A.3.b.iv-7",
                    "1.A.3.b.iv-8",
                ]
            ],
        },
        "1.A.3.b.v": {
            "title": "Other",
            "alternative_codes": [
                "9083",
                "1A3bv",
                "1 A 3 b v",
                "1.A.3.b.v-10510",
                "9083-10510",
            ],
            "info": {"numerical_ids": ["9083"]},
            "children": [
                [
                    "1.A.3.b.v-1",
                    "1.A.3.b.v-2",
                    "1.A.3.b.v-3",
                    "1.A.3.b.v-4",
                    "1.A.3.b.v-5",
                    "1.A.3.b.v-6",
                    "1.A.3.b.v-7",
                    "1.A.3.b.v-8",
                ]
            ],
        },
        "1.A.3.c": {
            "title": "Railways",
            "alternative_codes": [
                "8924",
                "1A3c",
                "1 A 3 c",
                "1.A.3.c-10510",
                "8924-10510",
            ],
            "info": {"numerical_ids": ["8924"]},
            "children": [
                ["1.A.3.c-1", "1.A.3.c-2", "1.A.3.c-3", "1.A.3.c-4", "1.A.3.c-5"]
            ],
        },
        "1.A.3.d": {
            "title": "Domestic Navigation",
            "alternative_codes": [
                "9670",
                "1A3d",
                "1 A 3 d",
                "1.A.3.d-10510",
                "9670-10510",
            ],
            "info": {"numerical_ids": ["9670"]},
            "children": [
                [
                    "1.A.3.d-1",
                    "1.A.3.d-2",
                    "1.A.3.d-3",
                    "1.A.3.d-4",
                    "1.A.3.d-5",
                    "1.A.3.d-6",
                    "1.A.3.d-7",
                    "1.A.3.d-8",
                ]
            ],
        },
        "1.A.3.e": {
            "title": "Other Transportation",
            "alternative_codes": [
                "8456",
                "1A3e",
                "1 A 3 e",
                "1.A.3.e-10510",
                "8456-10510",
            ],
            "info": {"numerical_ids": ["8456"]},
            "children": [
                ["1.A.3.e.i", "1.A.3.e.ii"],
                ["1.A.3.e-1", "1.A.3.e-2", "1.A.3.e-3", "1.A.3.e-4", "1.A.3.e-5"],
            ],
        },
        "1.A.3.e.i": {
            "title": "Pipeline Transport",
            "alternative_codes": [
                "9504",
                "1A3ei",
                "1 A 3 e i",
                "1.A.3.e.i-10510",
                "9504-10510",
            ],
            "info": {"numerical_ids": ["9504"]},
            "children": [
                [
                    "1.A.3.e.i-1",
                    "1.A.3.e.i-2",
                    "1.A.3.e.i-3",
                    "1.A.3.e.i-4",
                    "1.A.3.e.i-5",
                ]
            ],
        },
        "1.A.3.e.ii": {
            "title": "Other",
            "alternative_codes": [
                "9935",
                "1A3eii",
                "1 A 3 e ii",
                "1.A.3.e.ii-10510",
                "9935-10510",
            ],
            "info": {"numerical_ids": ["9935"]},
            "children": [
                [
                    "1.A.3.e.ii-1",
                    "1.A.3.e.ii-2",
                    "1.A.3.e.ii-3",
                    "1.A.3.e.ii-4",
                    "1.A.3.e.ii-5",
                ]
            ],
        },
        "1.A.4": {
            "title": "Other Sectors",
            "alternative_codes": ["9815", "1A4", "1 A 4", "1.A.4-10510", "9815-10510"],
            "info": {"numerical_ids": ["9815"]},
            "children": [
                ["1.A.4.a", "1.A.4.b", "1.A.4.c"],
                ["1.A.4-1", "1.A.4-2", "1.A.4-3", "1.A.4-4", "1.A.4-5", "1.A.4-6"],
            ],
        },
        "1.A.4.a": {
            "title": "Commercial/Institutional",
            "alternative_codes": [
                "8597",
                "1A4a",
                "1 A 4 a",
                "1.A.4.a-10510",
                "8597-10510",
            ],
            "info": {"numerical_ids": ["8597"]},
            "children": [
                ["1.A.4.a.i", "1.A.4.a.ii", "1.A.4.a.iii"],
                [
                    "1.A.4.a-1",
                    "1.A.4.a-2",
                    "1.A.4.a-3",
                    "1.A.4.a-4",
                    "1.A.4.a-5",
                    "1.A.4.a-6",
                ],
            ],
        },
        "1.A.4.a.i": {
            "title": "Stationary Combustion",
            "alternative_codes": [
                "8216",
                "1A4ai",
                "1 A 4 a i",
                "1.A.4.a.i-10510",
                "8216-10510",
            ],
            "info": {"numerical_ids": ["8216"]},
            "children": [
                [
                    "1.A.4.a.i-1",
                    "1.A.4.a.i-2",
                    "1.A.4.a.i-3",
                    "1.A.4.a.i-4",
                    "1.A.4.a.i-5",
                    "1.A.4.a.i-6",
                ]
            ],
        },
        "1.A.4.a.ii": {
            "title": "Off-road Vehicles and Other Machinery",
            "alternative_codes": [
                "8251",
                "1A4aii",
                "1 A 4 a ii",
                "1.A.4.a.ii-10510",
                "8251-10510",
            ],
            "info": {"numerical_ids": ["8251"]},
            "children": [
                [
                    "1.A.4.a.ii-1",
                    "1.A.4.a.ii-2",
                    "1.A.4.a.ii-3",
                    "1.A.4.a.ii-4",
                    "1.A.4.a.ii-5",
                ]
            ],
        },
        "1.A.4.a.iii": {
            "title": "Other",
            "alternative_codes": [
                "8223",
                "1A4aiii",
                "1 A 4 a iii",
                "1.A.4.a.iii-10510",
                "8223-10510",
            ],
            "info": {"numerical_ids": ["8223"]},
            "children": [
                [
                    "1.A.4.a.iii-1",
                    "1.A.4.a.iii-2",
                    "1.A.4.a.iii-3",
                    "1.A.4.a.iii-4",
                    "1.A.4.a.iii-5",
                    "1.A.4.a.iii-6",
                ]
            ],
        },
        "1.A.4.b": {
            "title": "Residential",
            "alternative_codes": [
                "9823",
                "1A4b",
                "1 A 4 b",
                "1.A.4.b-10510",
                "9823-10510",
            ],
            "info": {"numerical_ids": ["9823"]},
            "children": [
                ["1.A.4.b.i", "1.A.4.b.ii", "1.A.4.b.iii"],
                [
                    "1.A.4.b-1",
                    "1.A.4.b-2",
                    "1.A.4.b-3",
                    "1.A.4.b-4",
                    "1.A.4.b-5",
                    "1.A.4.b-6",
                ],
            ],
        },
        "1.A.4.b.i": {
            "title": "Stationary Combustion",
            "alternative_codes": [
                "8609",
                "1A4bi",
                "1 A 4 b i",
                "1.A.4.b.i-10510",
                "8609-10510",
            ],
            "info": {"numerical_ids": ["8609"]},
            "children": [
                [
                    "1.A.4.b.i-1",
                    "1.A.4.b.i-2",
                    "1.A.4.b.i-3",
                    "1.A.4.b.i-4",
                    "1.A.4.b.i-5",
                    "1.A.4.b.i-6",
                ]
            ],
        },
        "1.A.4.b.ii": {
            "title": "Off-road Vehicles and Other Machinery",
            "alternative_codes": [
                "10435",
                "1A4bii",
                "1 A 4 b ii",
                "1.A.4.b.ii-10510",
                "10435-10510",
            ],
            "info": {"numerical_ids": ["10435"]},
            "children": [
                [
                    "1.A.4.b.ii-1",
                    "1.A.4.b.ii-2",
                    "1.A.4.b.ii-3",
                    "1.A.4.b.ii-4",
                    "1.A.4.b.ii-5",
                ]
            ],
        },
        "1.A.4.b.iii": {
            "title": "Other",
            "alternative_codes": [
                "8632",
                "1A4biii",
                "1 A 4 b iii",
                "1.A.4.b.iii-10510",
                "8632-10510",
            ],
            "info": {"numerical_ids": ["8632"]},
            "children": [
                [
                    "1.A.4.b.iii-1",
                    "1.A.4.b.iii-2",
                    "1.A.4.b.iii-3",
                    "1.A.4.b.iii-4",
                    "1.A.4.b.iii-5",
                    "1.A.4.b.iii-6",
                ]
            ],
        },
        "1.A.4.c": {
            "title": "Agriculture/Forestry/Fishing",
            "alternative_codes": [
                "8554",
                "1A4c",
                "1 A 4 c",
                "1.A.4.c-10510",
                "8554-10510",
            ],
            "info": {"numerical_ids": ["8554"]},
            "children": [
                ["1.A.4.c.i", "1.A.4.c.ii", "1.A.4.c.iii"],
                [
                    "1.A.4.c-1",
                    "1.A.4.c-2",
                    "1.A.4.c-3",
                    "1.A.4.c-4",
                    "1.A.4.c-5",
                    "1.A.4.c-6",
                ],
            ],
        },
        "1.A.4.c.i": {
            "title": "Stationary",
            "alternative_codes": [
                "8364",
                "1A4ci",
                "1 A 4 c i",
                "1.A.4.c.i-10510",
                "8364-10510",
            ],
            "info": {"numerical_ids": ["8364"]},
            "children": [
                [
                    "1.A.4.c.i-1",
                    "1.A.4.c.i-2",
                    "1.A.4.c.i-3",
                    "1.A.4.c.i-4",
                    "1.A.4.c.i-5",
                    "1.A.4.c.i-6",
                ]
            ],
        },
        "1.A.4.c.ii": {
            "title": "Off-road Vehicles and Other Machinery",
            "alternative_codes": [
                "10080",
                "1A4cii",
                "1 A 4 c ii",
                "1.A.4.c.ii-10510",
                "10080-10510",
            ],
            "info": {"numerical_ids": ["10080"]},
            "children": [
                [
                    "1.A.4.c.ii-1",
                    "1.A.4.c.ii-2",
                    "1.A.4.c.ii-3",
                    "1.A.4.c.ii-4",
                    "1.A.4.c.ii-5",
                    "1.A.4.c.ii-6",
                    "1.A.4.c.ii-7",
                    "1.A.4.c.ii-8",
                ]
            ],
        },
        "1.A.4.c.iii": {
            "title": "Fishing",
            "alternative_codes": [
                "9812",
                "1A4ciii",
                "1 A 4 c iii",
                "1.A.4.c.iii-10510",
                "9812-10510",
            ],
            "info": {"numerical_ids": ["9812"]},
            "children": [
                [
                    "1.A.4.c.iii-1",
                    "1.A.4.c.iii-2",
                    "1.A.4.c.iii-3",
                    "1.A.4.c.iii-4",
                    "1.A.4.c.iii-5",
                    "1.A.4.c.iii-6",
                    "1.A.4.c.iii-7",
                    "1.A.4.c.iii-8",
                ]
            ],
        },
        "1.A.5": {
            "title": "Other (Not specified elsewhere)",
            "alternative_codes": [
                "10273",
                "1A5",
                "1 A 5",
                "1.A.5-10510",
                "10273-10510",
            ],
            "info": {"numerical_ids": ["10273"]},
            "children": [
                ["1.A.5.a", "1.A.5.b"],
                ["1.A.5-1", "1.A.5-2", "1.A.5-3", "1.A.5-4", "1.A.5-5", "1.A.5-6"],
            ],
        },
        "1.A.5.a": {
            "title": "Stationary",
            "alternative_codes": [
                "9861",
                "1A5a",
                "1 A 5 a",
                "1.A.5.a-10510",
                "9861-10510",
            ],
            "info": {"numerical_ids": ["9861"]},
            "children": [
                [
                    "1.A.5.a-1",
                    "1.A.5.a-2",
                    "1.A.5.a-3",
                    "1.A.5.a-4",
                    "1.A.5.a-5",
                    "1.A.5.a-6",
                ]
            ],
        },
        "1.A.5.b": {
            "title": "Mobile",
            "alternative_codes": [
                "9101",
                "1A5b",
                "1 A 5 b",
                "1.A.5.b-10510",
                "9101-10510",
            ],
            "info": {"numerical_ids": ["9101"]},
            "children": [
                ["1.A.5.b-1", "1.A.5.b-2", "1.A.5.b-3", "1.A.5.b-4", "1.A.5.b-5"]
            ],
        },
        "1.AA": {
            "title": "Fuel Combustion - Sectoral approach",
            "alternative_codes": [
                "9089",
                "1.A",
                "1A",
                "1 A",
                "1AA",
                "1 AA",
                "1.AA-10510",
                "9089-10510",
            ],
            "info": {"numerical_ids": ["9089"]},
            "children": [
                ["1.A.1", "1.A.2", "1.A.3", "1.A.4", "1.A.5", "11026"],
                ["1.AA-1", "1.AA-2", "1.AA-3", "1.AA-4", "1.AA-5", "1.AA-6"],
            ],
        },
        "1.AB": {
            "title": "Fuel Combustion - Reference Approach",
            "alternative_codes": ["8533", "1AB", "1 AB", "1.AB-10510", "8533-10510"],
            "info": {"numerical_ids": ["8533"]},
            "children": [
                [
                    "1.AB-1",
                    "1.AB-10",
                    "1.AB-11",
                    "1.AB-12",
                    "1.AB-13",
                    "1.AB-14",
                    "1.AB-15",
                    "1.AB-16",
                    "1.AB-17",
                    "1.AB-18",
                    "1.AB-19",
                    "1.AB-2",
                    "1.AB-20",
                    "1.AB-21",
                    "1.AB-22",
                    "1.AB-23",
                    "1.AB-24",
                    "1.AB-25",
                    "1.AB-26",
                    "1.AB-27",
                    "1.AB-28",
                    "1.AB-29",
                    "1.AB-3",
                    "1.AB-30",
                    "1.AB-31",
                    "1.AB-32",
                    "1.AB-33",
                    "1.AB-34",
                    "1.AB-35",
                    "1.AB-36",
                    "1.AB-37",
                    "1.AB-38",
                    "1.AB-39",
                    "1.AB-4",
                    "1.AB-40",
                    "1.AB-41",
                    "1.AB-5",
                    "1.AB-6",
                    "1.AB-7",
                    "1.AB-8",
                    "1.AB-9",
                ]
            ],
        },
        "1.AD": {
            "title": "Feedstocks, Reductants and Other Non-energy Use of Fuels",
            "alternative_codes": ["8731", "1AD", "1 AD", "1.AD-10510", "8731-10510"],
            "info": {"numerical_ids": ["8731"]},
            "children": [
                [
                    "1.AD-1",
                    "1.AD-10",
                    "1.AD-11",
                    "1.AD-12",
                    "1.AD-13",
                    "1.AD-14",
                    "1.AD-15",
                    "1.AD-16",
                    "1.AD-17",
                    "1.AD-18",
                    "1.AD-19",
                    "1.AD-2",
                    "1.AD-20",
                    "1.AD-21",
                    "1.AD-22",
                    "1.AD-23",
                    "1.AD-24",
                    "1.AD-25",
                    "1.AD-26",
                    "1.AD-27",
                    "1.AD-28",
                    "1.AD-29",
                    "1.AD-3",
                    "1.AD-30",
                    "1.AD-31",
                    "1.AD-32",
                    "1.AD-33",
                    "1.AD-34",
                    "1.AD-35",
                    "1.AD-4",
                    "1.AD-5",
                    "1.AD-6",
                    "1.AD-7",
                    "1.AD-8",
                    "1.AD-9",
                ]
            ],
        },
        "1.B": {
            "title": "Fugitive Emissions from Fuels",
            "alternative_codes": ["9374", "1B", "1 B", "1.B-10510", "9374-10510"],
            "info": {"numerical_ids": ["9374"]},
            "children": [["1.B.1", "1.B.2"]],
        },
        "1.B.1": {
            "title": "Solid Fuels",
            "alternative_codes": ["9455", "1B1", "1 B 1", "1.B.1-10510", "9455-10510"],
            "info": {"numerical_ids": ["9455"]},
            "children": [["1.B.1.a", "1.B.1.b", "1.B.1.c"]],
        },
        "1.B.1.a": {
            "title": "Coal Mining and Handling",
            "alternative_codes": [
                "9835",
                "1B1a",
                "1 B 1 a",
                "1.B.1.a-10510",
                "9835-10510",
            ],
            "info": {"numerical_ids": ["9835"]},
            "children": [["1.B.1.a.i", "1.B.1.a.ii"]],
        },
        "1.B.1.a.i": {
            "title": "Underground Mines",
            "alternative_codes": [
                "9116",
                "1B1ai",
                "1 B 1 a i",
                "1.B.1.a.i-10510",
                "9116-10510",
            ],
            "info": {"numerical_ids": ["9116"]},
            "children": [["1.B.1.a.i.1", "1.B.1.a.i.2", "1.B.1.a.i.3"]],
        },
        "1.B.1.a.i.1": {
            "title": "Mining Activities",
            "alternative_codes": [
                "9933",
                "1B1ai1",
                "1 B 1 a i 1",
                "1.B.1.a.i.1-10510",
                "9933-10510",
            ],
            "info": {"numerical_ids": ["9933"]},
        },
        "1.B.1.a.i.2": {
            "title": "Post-Mining Activities",
            "alternative_codes": [
                "9427",
                "1B1ai2",
                "1 B 1 a i 2",
                "1.B.1.a.i.2-10510",
                "9427-10510",
            ],
            "info": {"numerical_ids": ["9427"]},
        },
        "1.B.1.a.i.3": {
            "title": "Abandoned Underground Mines",
            "alternative_codes": [
                "8211",
                "1B1ai3",
                "1 B 1 a i 3",
                "1.B.1.a.i.3-10510",
                "8211-10510",
            ],
            "info": {"numerical_ids": ["8211"]},
        },
        "1.B.1.a.ii": {
            "title": "Surface Mines",
            "alternative_codes": [
                "8573",
                "1B1aii",
                "1 B 1 a ii",
                "1.B.1.a.ii-10510",
                "8573-10510",
            ],
            "info": {"numerical_ids": ["8573"]},
            "children": [["1.B.1.a.ii.1", "1.B.1.a.ii.2"]],
        },
        "1.B.1.a.ii.1": {
            "title": "Mining Activities",
            "alternative_codes": [
                "10282",
                "1B1aii1",
                "1 B 1 a ii 1",
                "1.B.1.a.ii.1-10510",
                "10282-10510",
            ],
            "info": {"numerical_ids": ["10282"]},
        },
        "1.B.1.a.ii.2": {
            "title": "Post-Mining Activities",
            "alternative_codes": [
                "9601",
                "1B1aii2",
                "1 B 1 a ii 2",
                "1.B.1.a.ii.2-10510",
                "9601-10510",
            ],
            "info": {"numerical_ids": ["9601"]},
        },
        "1.B.1.b": {
            "title": "Solid Fuel Transformation",
            "alternative_codes": [
                "8300",
                "1B1b",
                "1 B 1 b",
                "1.B.1.b-10510",
                "8300-10510",
            ],
            "info": {"numerical_ids": ["8300"]},
        },
        "1.B.1.c": {
            "title": "Other",
            "alternative_codes": [
                "8964",
                "1B1c",
                "1 B 1 c",
                "1.B.1.c-10510",
                "8964-10510",
            ],
            "info": {"numerical_ids": ["8964"]},
        },
        "1.B.2": {
            "title": "Oil and Natural Gas and Other Emissions from Energy Production",
            "alternative_codes": ["8806", "1B2", "1 B 2", "1.B.2-10510", "8806-10510"],
            "info": {"numerical_ids": ["8806"]},
            "children": [["1.B.2.a", "1.B.2.b", "1.B.2.c", "1.B.2.d"]],
        },
        "1.B.2.a": {
            "title": "Oil",
            "alternative_codes": [
                "9822",
                "1B2a",
                "1 B 2 a",
                "1.B.2.a-10510",
                "9822-10510",
            ],
            "info": {"numerical_ids": ["9822"]},
            "children": [
                [
                    "1.B.2.a.i",
                    "1.B.2.a.ii",
                    "1.B.2.a.iii",
                    "1.B.2.a.iv",
                    "1.B.2.a.v",
                    "1.B.2.a.vi",
                ]
            ],
        },
        "1.B.2.a.i": {
            "title": "Exploration",
            "alternative_codes": [
                "8165",
                "1B2ai",
                "1 B 2 a i",
                "1.B.2.a.i-10510",
                "8165-10510",
            ],
            "info": {"numerical_ids": ["8165"]},
        },
        "1.B.2.a.ii": {
            "title": "Production",
            "alternative_codes": [
                "10078",
                "1B2aii",
                "1 B 2 a ii",
                "1.B.2.a.ii-10510",
                "10078-10510",
            ],
            "info": {"numerical_ids": ["10078"]},
        },
        "1.B.2.a.iii": {
            "title": "Transport",
            "alternative_codes": [
                "9550",
                "1B2aiii",
                "1 B 2 a iii",
                "1.B.2.a.iii-10510",
                "9550-10510",
            ],
            "info": {"numerical_ids": ["9550"]},
        },
        "1.B.2.a.iv": {
            "title": "Refining / Storage",
            "alternative_codes": [
                "9891",
                "1B2aiv",
                "1 B 2 a iv",
                "1.B.2.a.iv-10510",
                "9891-10510",
            ],
            "info": {"numerical_ids": ["9891"]},
        },
        "1.B.2.a.v": {
            "title": "Distribution of Oil Products",
            "alternative_codes": [
                "8371",
                "1B2av",
                "1 B 2 a v",
                "1.B.2.a.v-10510",
                "8371-10510",
            ],
            "info": {"numerical_ids": ["8371"]},
        },
        "1.B.2.a.vi": {
            "title": "Other",
            "alternative_codes": [
                "8228",
                "1B2avi",
                "1 B 2 a vi",
                "1.B.2.a.vi-10510",
                "8228-10510",
            ],
            "info": {"numerical_ids": ["8228"]},
        },
        "1.B.2.b": {
            "title": "Natural Gas",
            "alternative_codes": [
                "8493",
                "1B2b",
                "1 B 2 b",
                "1.B.2.b-10510",
                "8493-10510",
            ],
            "info": {"numerical_ids": ["8493"]},
            "children": [
                [
                    "1.B.2.b.i",
                    "1.B.2.b.ii",
                    "1.B.2.b.iii",
                    "1.B.2.b.iv",
                    "1.B.2.b.v",
                    "1.B.2.b.vi",
                ]
            ],
        },
        "1.B.2.b.i": {
            "title": "Exploration",
            "alternative_codes": [
                "9314",
                "1B2bi",
                "1 B 2 b i",
                "1.B.2.b.i-10510",
                "9314-10510",
            ],
            "info": {"numerical_ids": ["9314"]},
        },
        "1.B.2.b.ii": {
            "title": "Production",
            "alternative_codes": [
                "8474",
                "1B2bii",
                "1 B 2 b ii",
                "1.B.2.b.ii-10510",
                "8474-10510",
            ],
            "info": {"numerical_ids": ["8474"]},
        },
        "1.B.2.b.iii": {
            "title": "Processing",
            "alternative_codes": [
                "9999",
                "1B2biii",
                "1 B 2 b iii",
                "1.B.2.b.iii-10510",
                "9999-10510",
            ],
            "info": {"numerical_ids": ["9999"]},
        },
        "1.B.2.b.iv": {
            "title": "Transmission and Storage",
            "alternative_codes": [
                "9902",
                "1B2biv",
                "1 B 2 b iv",
                "1.B.2.b.iv-10510",
                "9902-10510",
            ],
            "info": {"numerical_ids": ["9902"]},
        },
        "1.B.2.b.v": {
            "title": "Distribution",
            "alternative_codes": [
                "9728",
                "1B2bv",
                "1 B 2 b v",
                "1.B.2.b.v-10510",
                "9728-10510",
            ],
            "info": {"numerical_ids": ["9728"]},
        },
        "1.B.2.b.vi": {
            "title": "Other",
            "alternative_codes": [
                "9974",
                "1B2bvi",
                "1 B 2 b vi",
                "1.B.2.b.vi-10510",
                "9974-10510",
            ],
            "info": {"numerical_ids": ["9974"]},
        },
        "1.B.2.c": {
            "title": "Venting and Flaring",
            "alternative_codes": [
                "8333",
                "1B2c",
                "1 B 2 c",
                "1.B.2.c-10510",
                "8333-10510",
            ],
            "info": {"numerical_ids": ["8333"]},
            "children": [["1.B.2.c.i", "1.B.2.c.ii"]],
        },
        "1.B.2.c.i": {
            "title": "Venting",
            "alternative_codes": [
                "10303",
                "1B2ci",
                "1 B 2 c i",
                "1.B.2.c.i-10510",
                "10303-10510",
            ],
            "info": {"numerical_ids": ["10303"]},
            "children": [["1.B.2.c.i.1", "1.B.2.c.i.2", "1.B.2.c.i.3"]],
        },
        "1.B.2.c.i.1": {
            "title": "Oil",
            "alternative_codes": [
                "9827",
                "1B2ci1",
                "1 B 2 c i 1",
                "1.B.2.c.i.1-10510",
                "9827-10510",
            ],
            "info": {"numerical_ids": ["9827"]},
        },
        "1.B.2.c.i.2": {
            "title": "Gas",
            "alternative_codes": [
                "10239",
                "1B2ci2",
                "1 B 2 c i 2",
                "1.B.2.c.i.2-10510",
                "10239-10510",
            ],
            "info": {"numerical_ids": ["10239"]},
        },
        "1.B.2.c.i.3": {
            "title": "Combined",
            "alternative_codes": [
                "8576",
                "1B2ci3",
                "1 B 2 c i 3",
                "1.B.2.c.i.3-10510",
                "8576-10510",
            ],
            "info": {"numerical_ids": ["8576"]},
        },
        "1.B.2.c.ii": {
            "title": "Flaring",
            "alternative_codes": [
                "10392",
                "1B2cii",
                "1 B 2 c ii",
                "1.B.2.c.ii-10510",
                "10392-10510",
            ],
            "info": {"numerical_ids": ["10392"]},
            "children": [["1.B.2.c.ii.1", "1.B.2.c.ii.2", "1.B.2.c.ii.3"]],
        },
        "1.B.2.c.ii.1": {
            "title": "Oil",
            "alternative_codes": [
                "9210",
                "1B2cii1",
                "1 B 2 c ii 1",
                "1.B.2.c.ii.1-10510",
                "9210-10510",
            ],
            "info": {"numerical_ids": ["9210"]},
        },
        "1.B.2.c.ii.2": {
            "title": "Gas",
            "alternative_codes": [
                "8904",
                "1B2cii2",
                "1 B 2 c ii 2",
                "1.B.2.c.ii.2-10510",
                "8904-10510",
            ],
            "info": {"numerical_ids": ["8904"]},
        },
        "1.B.2.c.ii.3": {
            "title": "Combined",
            "alternative_codes": [
                "9824",
                "1B2cii3",
                "1 B 2 c ii 3",
                "1.B.2.c.ii.3-10510",
                "9824-10510",
            ],
            "info": {"numerical_ids": ["9824"]},
        },
        "1.B.2.d": {
            "title": "Other",
            "alternative_codes": [
                "9077",
                "1B2d",
                "1 B 2 d",
                "1.B.2.d-10510",
                "9077-10510",
            ],
            "info": {"numerical_ids": ["9077"]},
        },
        "1.C": {
            "title": "CO₂ Transport and Storage",
            "alternative_codes": ["9070", "1C", "1 C", "1.C-10510", "9070-10510"],
            "info": {"numerical_ids": ["9070"]},
            "children": [["1.C.1", "1.C.2", "1.C.3", "11029"]],
        },
        "1.C.1": {
            "title": "Transport of CO₂",
            "alternative_codes": ["9365", "1C1", "1 C 1", "1.C.1-10510", "9365-10510"],
            "info": {"numerical_ids": ["9365"]},
            "children": [["1.C.1.a", "1.C.1.b", "1.C.1.c"]],
        },
        "1.C.1.a": {
            "title": "Pipelines",
            "alternative_codes": [
                "9769",
                "1C1a",
                "1 C 1 a",
                "1.C.1.a-10510",
                "9769-10510",
            ],
            "info": {"numerical_ids": ["9769"]},
        },
        "1.C.1.b": {
            "title": "Ships",
            "alternative_codes": [
                "10197",
                "1C1b",
                "1 C 1 b",
                "1.C.1.b-10510",
                "10197-10510",
            ],
            "info": {"numerical_ids": ["10197"]},
        },
        "1.C.1.c": {
            "title": "Other",
            "alternative_codes": [
                "9366",
                "1C1c",
                "1 C 1 c",
                "1.C.1.c-10510",
                "9366-10510",
            ],
            "info": {"numerical_ids": ["9366"]},
        },
        "1.C.2": {
            "title": "Injection and Storage",
            "alternative_codes": ["9474", "1C2", "1 C 2", "1.C.2-10510", "9474-10510"],
            "info": {"numerical_ids": ["9474"]},
            "children": [["1.C.2.a", "1.C.2.b"]],
        },
        "1.C.2.a": {
            "title": "Injection",
            "alternative_codes": [
                "8741",
                "1C2a",
                "1 C 2 a",
                "1.C.2.a-10510",
                "8741-10510",
            ],
            "info": {"numerical_ids": ["8741"]},
        },
        "1.C.2.b": {
            "title": "Storage",
            "alternative_codes": [
                "10333",
                "1C2b",
                "1 C 2 b",
                "1.C.2.b-10510",
                "10333-10510",
            ],
            "info": {"numerical_ids": ["10333"]},
        },
        "1.C.3": {
            "title": "Other",
            "alternative_codes": ["9330", "1C3", "1 C 3", "1.C.3-10510", "9330-10510"],
            "info": {"numerical_ids": ["9330"]},
        },
        "2": {
            "title": "Industrial Processes and Product Use",
            "alternative_codes": [
                "2.",
                "10393",
                "10482",
                "2-10510",
                "10393-10510",
                "10482-10510",
            ],
            "info": {"numerical_ids": ["10393", "10482"]},
            "children": [["2.A", "2.B", "2.C", "2.D", "2.E", "2.F", "2.G", "2.H"]],
        },
        "2.A": {
            "title": "Mineral Industry",
            "alternative_codes": ["8452", "2A", "2 A", "2.A-10510", "8452-10510"],
            "info": {"numerical_ids": ["8452"]},
            "children": [["2.A.1", "2.A.2", "2.A.3", "2.A.4"]],
        },
        "2.A.1": {
            "title": "Cement Production",
            "alternative_codes": ["8787", "2A1", "2 A 1", "2.A.1-10510", "8787-10510"],
            "info": {"numerical_ids": ["8787"]},
        },
        "2.A.2": {
            "title": "Lime Production",
            "alternative_codes": ["8702", "2A2", "2 A 2", "2.A.2-10510", "8702-10510"],
            "info": {"numerical_ids": ["8702"]},
        },
        "2.A.3": {
            "title": "Glass production",
            "alternative_codes": ["8579", "2A3", "2 A 3", "2.A.3-10510", "8579-10510"],
            "info": {"numerical_ids": ["8579"]},
        },
        "2.A.4": {
            "title": "Other Process Uses of Carbonates",
            "alternative_codes": ["9731", "2A4", "2 A 4", "2.A.4-10510", "9731-10510"],
            "info": {"numerical_ids": ["9731"]},
            "children": [["2.A.4.a", "2.A.4.b", "2.A.4.c", "2.A.4.d"]],
        },
        "2.A.4.a": {
            "title": "Ceramics",
            "alternative_codes": [
                "8539",
                "2A4a",
                "2 A 4 a",
                "2.A.4.a-10510",
                "8539-10510",
            ],
            "info": {"numerical_ids": ["8539"]},
        },
        "2.A.4.b": {
            "title": "Other Uses of Soda Ash",
            "alternative_codes": [
                "9452",
                "2A4b",
                "2 A 4 b",
                "2.A.4.b-10510",
                "9452-10510",
            ],
            "info": {"numerical_ids": ["9452"]},
        },
        "2.A.4.c": {
            "title": "Non-metallurgical Magnesium Production",
            "alternative_codes": [
                "10101",
                "2A4c",
                "2 A 4 c",
                "2.A.4.c-10510",
                "10101-10510",
            ],
            "info": {"numerical_ids": ["10101"]},
        },
        "2.A.4.d": {
            "title": "Other",
            "alternative_codes": [
                "9342",
                "2A4d",
                "2 A 4 d",
                "2.A.4.d-10510",
                "9342-10510",
            ],
            "info": {"numerical_ids": ["9342"]},
        },
        "2.B": {
            "title": "Chemical Industry",
            "alternative_codes": ["9304", "2B", "2 B", "2.B-10510", "9304-10510"],
            "info": {"numerical_ids": ["9304"]},
            "children": [
                [
                    "2.B.1",
                    "2.B.10",
                    "2.B.2",
                    "2.B.3",
                    "2.B.4",
                    "2.B.5",
                    "2.B.6",
                    "2.B.7",
                    "2.B.8",
                    "2.B.9",
                ]
            ],
        },
        "2.B.1": {
            "title": "Ammonia Production",
            "alternative_codes": ["9658", "2B1", "2 B 1", "2.B.1-10510", "9658-10510"],
            "info": {"numerical_ids": ["9658"]},
        },
        "2.B.2": {
            "title": "Nitric Acid Production",
            "alternative_codes": ["9410", "2B2", "2 B 2", "2.B.2-10510", "9410-10510"],
            "info": {"numerical_ids": ["9410"]},
        },
        "2.B.3": {
            "title": "Adipic Acid Production",
            "alternative_codes": ["8468", "2B3", "2 B 3", "2.B.3-10510", "8468-10510"],
            "info": {"numerical_ids": ["8468"]},
        },
        "2.B.4": {
            "title": "Caprolactam, Glyoxal and Glyoxylic Acid Production",
            "alternative_codes": ["8544", "2B4", "2 B 4", "2.B.4-10510", "8544-10510"],
            "info": {"numerical_ids": ["8544"]},
            "children": [["2.B.4.a", "2.B.4.b", "2.B.4.c"]],
        },
        "2.B.4.a": {
            "title": "Caprolactam",
            "alternative_codes": [
                "9515",
                "2B4a",
                "2 B 4 a",
                "2.B.4.a-10510",
                "9515-10510",
            ],
            "info": {"numerical_ids": ["9515"]},
        },
        "2.B.4.b": {
            "title": "Glyoxal",
            "alternative_codes": [
                "9564",
                "2B4b",
                "2 B 4 b",
                "2.B.4.b-10510",
                "9564-10510",
            ],
            "info": {"numerical_ids": ["9564"]},
        },
        "2.B.4.c": {
            "title": "Glyoxylic Acid",
            "alternative_codes": [
                "8789",
                "2B4c",
                "2 B 4 c",
                "2.B.4.c-10510",
                "8789-10510",
            ],
            "info": {"numerical_ids": ["8789"]},
        },
        "2.B.5": {
            "title": "Carbide Production",
            "alternative_codes": ["9531", "2B5", "2 B 5", "2.B.5-10510", "9531-10510"],
            "info": {"numerical_ids": ["9531"]},
            "children": [["2.B.5.a", "2.B.5.b"]],
        },
        "2.B.5.a": {
            "title": "Silicon Carbide",
            "alternative_codes": [
                "9683",
                "2B5a",
                "2 B 5 a",
                "2.B.5.a-10510",
                "9683-10510",
            ],
            "info": {"numerical_ids": ["9683"]},
        },
        "2.B.5.b": {
            "title": "Calcium Carbide",
            "alternative_codes": [
                "9206",
                "2B5b",
                "2 B 5 b",
                "2.B.5.b-10510",
                "9206-10510",
            ],
            "info": {"numerical_ids": ["9206"]},
        },
        "2.B.6": {
            "title": "Titanium Dioxide Production",
            "alternative_codes": ["9917", "2B6", "2 B 6", "2.B.6-10510", "9917-10510"],
            "info": {"numerical_ids": ["9917"]},
        },
        "2.B.7": {
            "title": "Soda Ash Production",
            "alternative_codes": ["8530", "2B7", "2 B 7", "2.B.7-10510", "8530-10510"],
            "info": {"numerical_ids": ["8530"]},
        },
        "2.B.8": {
            "title": "Petrochemical and Carbon Black Production",
            "alternative_codes": ["9000", "2B8", "2 B 8", "2.B.8-10510", "9000-10510"],
            "info": {"numerical_ids": ["9000"]},
            "children": [
                [
                    "2.B.8.a",
                    "2.B.8.b",
                    "2.B.8.c",
                    "2.B.8.d",
                    "2.B.8.e",
                    "2.B.8.f",
                    "2.B.8.g",
                ]
            ],
        },
        "2.B.8.a": {
            "title": "Methanol",
            "alternative_codes": [
                "8934",
                "2B8a",
                "2 B 8 a",
                "2.B.8.a-10510",
                "8934-10510",
            ],
            "info": {"numerical_ids": ["8934"]},
        },
        "2.B.8.b": {
            "title": "Ethylene",
            "alternative_codes": [
                "9146",
                "2B8b",
                "2 B 8 b",
                "2.B.8.b-10510",
                "9146-10510",
            ],
            "info": {"numerical_ids": ["9146"]},
        },
        "2.B.8.c": {
            "title": "Ethylene Dichloride and Vinyl Chloride Monomer",
            "alternative_codes": [
                "8686",
                "2B8c",
                "2 B 8 c",
                "2.B.8.c-10510",
                "8686-10510",
            ],
            "info": {"numerical_ids": ["8686"]},
        },
        "2.B.8.d": {
            "title": "Ethylene Oxide",
            "alternative_codes": [
                "9468",
                "2B8d",
                "2 B 8 d",
                "2.B.8.d-10510",
                "9468-10510",
            ],
            "info": {"numerical_ids": ["9468"]},
        },
        "2.B.8.e": {
            "title": "Acrylonitrile",
            "alternative_codes": [
                "9784",
                "2B8e",
                "2 B 8 e",
                "2.B.8.e-10510",
                "9784-10510",
            ],
            "info": {"numerical_ids": ["9784"]},
        },
        "2.B.8.f": {
            "title": "Carbon Black",
            "alternative_codes": [
                "8864",
                "2B8f",
                "2 B 8 f",
                "2.B.8.f-10510",
                "8864-10510",
            ],
            "info": {"numerical_ids": ["8864"]},
        },
        "2.B.8.g": {
            "title": "Other",
            "alternative_codes": [
                "9384",
                "2B8g",
                "2 B 8 g",
                "2.B.8.g-10510",
                "9384-10510",
            ],
            "info": {"numerical_ids": ["9384"]},
            "children": [["2.B.8.g.i", "2.B.8.g.ii"]],
        },
        "2.B.8.g.i": {
            "title": "Styrene",
            "alternative_codes": [
                "9941",
                "2B8gi",
                "2 B 8 g i",
                "2.B.8.g.i-10510",
                "9941-10510",
            ],
            "info": {"numerical_ids": ["9941"]},
        },
        "2.B.8.g.ii": {
            "title": "Other",
            "alternative_codes": [
                "8276",
                "2B8gii",
                "2 B 8 g ii",
                "2.B.8.g.ii-10510",
                "8276-10510",
            ],
            "info": {"numerical_ids": ["8276"]},
        },
        "2.B.9": {
            "title": "Fluorochemical Production",
            "alternative_codes": ["8884", "2B9", "2 B 9", "2.B.9-10510", "8884-10510"],
            "info": {"numerical_ids": ["8884"]},
            "children": [["2.B.9.a", "2.B.9.b"]],
        },
        "2.B.9.a": {
            "title": "By-Product Emissions",
            "alternative_codes": [
                "9517",
                "2B9a",
                "2 B 9 a",
                "2.B.9.a-10510",
                "9517-10510",
            ],
            "info": {"numerical_ids": ["9517"]},
            "children": [["2.B.9.a.i", "2.B.9.a.ii"]],
        },
        "2.B.9.a.i": {
            "title": "Production of HCFC-22",
            "alternative_codes": [
                "9992",
                "2B9ai",
                "2 B 9 a i",
                "2.B.9.a.i-10510",
                "9992-10510",
            ],
            "info": {"numerical_ids": ["9992"]},
        },
        "2.B.9.a.ii": {
            "title": "Other",
            "alternative_codes": [
                "8782",
                "2B9aii",
                "2 B 9 a ii",
                "2.B.9.a.ii-10510",
                "8782-10510",
            ],
            "info": {"numerical_ids": ["8782"]},
        },
        "2.B.9.b": {
            "title": "Fugitive Emissions",
            "alternative_codes": [
                "9938",
                "2B9b",
                "2 B 9 b",
                "2.B.9.b-10510",
                "9938-10510",
            ],
            "info": {"numerical_ids": ["9938"]},
            "children": [["2.B.9.b.i", "2.B.9.b.ii", "2.B.9.b.iii"]],
        },
        "2.B.9.b.i": {
            "title": "Production of HFC-134a",
            "alternative_codes": [
                "8427",
                "2B9bi",
                "2 B 9 b i",
                "2.B.9.b.i-10510",
                "8427-10510",
            ],
            "info": {"numerical_ids": ["8427"]},
        },
        "2.B.9.b.ii": {
            "title": "Production of SF₆",
            "alternative_codes": [
                "8150",
                "2B9bii",
                "2 B 9 b ii",
                "2.B.9.b.ii-10510",
                "8150-10510",
            ],
            "info": {"numerical_ids": ["8150"]},
        },
        "2.B.9.b.iii": {
            "title": "Other",
            "alternative_codes": [
                "8419",
                "2B9biii",
                "2 B 9 b iii",
                "2.B.9.b.iii-10510",
                "8419-10510",
            ],
            "info": {"numerical_ids": ["8419"]},
        },
        "2.B.10": {
            "title": "Other",
            "alternative_codes": [
                "9953",
                "2B10",
                "2 B 10",
                "2.B.10-10510",
                "9953-10510",
            ],
            "info": {"numerical_ids": ["9953"]},
        },
        "2.C": {
            "title": "Metal Industry",
            "alternative_codes": ["9064", "2C", "2 C", "2.C-10510", "9064-10510"],
            "info": {"numerical_ids": ["9064"]},
            "children": [
                ["2.C.1", "2.C.2", "2.C.3", "2.C.4", "2.C.5", "2.C.6", "2.C.7"]
            ],
        },
        "2.C.1": {
            "title": "Iron and Steel Production",
            "alternative_codes": ["8229", "2C1", "2 C 1", "2.C.1-10510", "8229-10510"],
            "info": {"numerical_ids": ["8229"]},
            "children": [
                ["2.C.1.a", "2.C.1.b", "2.C.1.c", "2.C.1.d", "2.C.1.e", "2.C.1.f"]
            ],
        },
        "2.C.1.a": {
            "title": "Steel",
            "alternative_codes": [
                "9540",
                "2C1a",
                "2 C 1 a",
                "2.C.1.a-10510",
                "9540-10510",
            ],
            "info": {"numerical_ids": ["9540"]},
        },
        "2.C.1.b": {
            "title": "Pig Iron",
            "alternative_codes": [
                "9567",
                "2C1b",
                "2 C 1 b",
                "2.C.1.b-10510",
                "9567-10510",
            ],
            "info": {"numerical_ids": ["9567"]},
        },
        "2.C.1.c": {
            "title": "Direct Reduced Iron",
            "alternative_codes": [
                "9679",
                "2C1c",
                "2 C 1 c",
                "2.C.1.c-10510",
                "9679-10510",
            ],
            "info": {"numerical_ids": ["9679"]},
        },
        "2.C.1.d": {
            "title": "Sinter",
            "alternative_codes": [
                "8962",
                "2C1d",
                "2 C 1 d",
                "2.C.1.d-10510",
                "8962-10510",
            ],
            "info": {"numerical_ids": ["8962"]},
        },
        "2.C.1.e": {
            "title": "Pellet",
            "alternative_codes": [
                "9387",
                "2C1e",
                "2 C 1 e",
                "2.C.1.e-10510",
                "9387-10510",
            ],
            "info": {"numerical_ids": ["9387"]},
        },
        "2.C.1.f": {
            "title": "Other",
            "alternative_codes": [
                "10223",
                "2C1f",
                "2 C 1 f",
                "2.C.1.f-10510",
                "10223-10510",
            ],
            "info": {"numerical_ids": ["10223"]},
        },
        "2.C.2": {
            "title": "Ferroalloys Production",
            "alternative_codes": [
                "10390",
                "2C2",
                "2 C 2",
                "2.C.2-10510",
                "10390-10510",
            ],
            "info": {"numerical_ids": ["10390"]},
        },
        "2.C.3": {
            "title": "Aluminium Production",
            "alternative_codes": [
                "10068",
                "2C3",
                "2 C 3",
                "2.C.3-10510",
                "10068-10510",
            ],
            "info": {"numerical_ids": ["10068"]},
            "children": [["2.C.3.a", "2.C.3.b", "2.C.3.c"]],
        },
        "2.C.3.a": {
            "title": "CO₂ Emissions",
            "alternative_codes": [
                "9079",
                "2C3a",
                "2 C 3 a",
                "2.C.3.a-10510",
                "9079-10510",
            ],
            "info": {"numerical_ids": ["9079"]},
        },
        "2.C.3.b": {
            "title": "By-Product Emissions",
            "alternative_codes": [
                "9445",
                "2C3b",
                "2 C 3 b",
                "2.C.3.b-10510",
                "9445-10510",
            ],
            "info": {"numerical_ids": ["9445"]},
        },
        "2.C.3.c": {
            "title": "F-gases Used in Foundries",
            "alternative_codes": [
                "9072",
                "2C3c",
                "2 C 3 c",
                "2.C.3.c-10510",
                "9072-10510",
            ],
            "info": {"numerical_ids": ["9072"]},
        },
        "2.C.4": {
            "title": "Magnesium Production",
            "alternative_codes": ["9635", "2C4", "2 C 4", "2.C.4-10510", "9635-10510"],
            "info": {"numerical_ids": ["9635"]},
        },
        "2.C.5": {
            "title": "Lead Production",
            "alternative_codes": [
                "10210",
                "2C5",
                "2 C 5",
                "2.C.5-10510",
                "10210-10510",
            ],
            "info": {"numerical_ids": ["10210"]},
        },
        "2.C.6": {
            "title": "Zinc Production",
            "alternative_codes": ["9667", "2C6", "2 C 6", "2.C.6-10510", "9667-10510"],
            "info": {"numerical_ids": ["9667"]},
        },
        "2.C.7": {
            "title": "Other",
            "alternative_codes": [
                "10447",
                "2C7",
                "2 C 7",
                "2.C.7-10510",
                "10447-10510",
            ],
            "info": {"numerical_ids": ["10447"]},
        },
        "2.D": {
            "title": "Non-energy Products from Fuels and Solvent Use",
            "alternative_codes": ["10094", "2D", "2 D", "2.D-10510", "10094-10510"],
            "info": {"numerical_ids": ["10094"]},
            "children": [["2.D.1", "2.D.2", "2.D.3"]],
        },
        "2.D.1": {
            "title": "Lubricant Use",
            "alternative_codes": ["8852", "2D1", "2 D 1", "2.D.1-10510", "8852-10510"],
            "info": {"numerical_ids": ["8852"]},
        },
        "2.D.2": {
            "title": "Paraffin Wax Use",
            "alternative_codes": ["8925", "2D2", "2 D 2", "2.D.2-10510", "8925-10510"],
            "info": {"numerical_ids": ["8925"]},
        },
        "2.D.3": {
            "title": "Other",
            "alternative_codes": ["8811", "2D3", "2 D 3", "2.D.3-10510", "8811-10510"],
            "info": {"numerical_ids": ["8811"]},
            "children": [["2.D.3.a", "2.D.3.b", "2.D.3.c", "2.D.3.d"]],
        },
        "2.D.3.a": {
            "title": "Solvent Use",
            "alternative_codes": [
                "10214",
                "2D3a",
                "2 D 3 a",
                "2.D.3.a-10510",
                "10214-10510",
            ],
            "info": {"numerical_ids": ["10214"]},
        },
        "2.D.3.b": {
            "title": "Road Paving with Asphalt",
            "alternative_codes": [
                "10044",
                "2D3b",
                "2 D 3 b",
                "2.D.3.b-10510",
                "10044-10510",
            ],
            "info": {"numerical_ids": ["10044"]},
        },
        "2.D.3.c": {
            "title": "Asphalt Roofing",
            "alternative_codes": [
                "8822",
                "2D3c",
                "2 D 3 c",
                "2.D.3.c-10510",
                "8822-10510",
            ],
            "info": {"numerical_ids": ["8822"]},
        },
        "2.D.3.d": {
            "title": "Other",
            "alternative_codes": [
                "8212",
                "2D3d",
                "2 D 3 d",
                "2.D.3.d-10510",
                "8212-10510",
            ],
            "info": {"numerical_ids": ["8212"]},
        },
        "2.E": {
            "title": "Electronics Industry",
            "alternative_codes": ["8938", "2E", "2 E", "2.E-10510", "8938-10510"],
            "info": {"numerical_ids": ["8938"]},
            "children": [["2.E.1", "2.E.2", "2.E.3", "2.E.4", "2.E.5"]],
        },
        "2.E.1": {
            "title": "Integrated Circuit or Semiconductor",
            "alternative_codes": [
                "10075",
                "2E1",
                "2 E 1",
                "2.E.1-10510",
                "10075-10510",
            ],
            "info": {"numerical_ids": ["10075"]},
        },
        "2.E.2": {
            "title": "TFT Flat Panel Display",
            "alternative_codes": [
                "10442",
                "2E2",
                "2 E 2",
                "2.E.2-10510",
                "10442-10510",
            ],
            "info": {"numerical_ids": ["10442"]},
        },
        "2.E.3": {
            "title": "Photovoltaics",
            "alternative_codes": ["8601", "2E3", "2 E 3", "2.E.3-10510", "8601-10510"],
            "info": {"numerical_ids": ["8601"]},
        },
        "2.E.4": {
            "title": "Heat Transfer Fluid",
            "alternative_codes": ["9911", "2E4", "2 E 4", "2.E.4-10510", "9911-10510"],
            "info": {"numerical_ids": ["9911"]},
        },
        "2.E.5": {
            "title": "Other",
            "alternative_codes": ["8434", "2E5", "2 E 5", "2.E.5-10510", "8434-10510"],
            "info": {"numerical_ids": ["8434"]},
        },
        "2.F": {
            "title": "Product Uses as Substitutes for ODS",
            "alternative_codes": ["8262", "2F", "2 F", "2.F-10510", "8262-10510"],
            "info": {"numerical_ids": ["8262"]},
            "children": [["2.F.1", "2.F.2", "2.F.3", "2.F.4", "2.F.5", "2.F.6"]],
        },
        "2.F.1": {
            "title": "Refrigeration and Air-conditioning",
            "alternative_codes": ["9207", "2F1", "2 F 1", "2.F.1-10510", "9207-10510"],
            "info": {"numerical_ids": ["9207"]},
            "children": [
                ["2.F.1.a", "2.F.1.b", "2.F.1.c", "2.F.1.d", "2.F.1.e", "2.F.1.f"]
            ],
        },
        "2.F.1.a": {
            "title": "Commercial Refrigeration",
            "alternative_codes": [
                "9129",
                "2F1a",
                "2 F 1 a",
                "2.F.1.a-10510",
                "9129-10510",
            ],
            "info": {"numerical_ids": ["9129"]},
            "children": [["2.F.1.a-m1", "2.F.1.a-m2", "2.F.1.a-m3"]],
        },
        "2.F.1.b": {
            "title": "Domestic Refrigeration",
            "alternative_codes": [
                "9780",
                "2F1b",
                "2 F 1 b",
                "2.F.1.b-10510",
                "9780-10510",
            ],
            "info": {"numerical_ids": ["9780"]},
            "children": [["2.F.1.b-m1", "2.F.1.b-m2", "2.F.1.b-m3"]],
        },
        "2.F.1.c": {
            "title": "Industrial Refrigeration",
            "alternative_codes": [
                "10252",
                "2F1c",
                "2 F 1 c",
                "2.F.1.c-10510",
                "10252-10510",
            ],
            "info": {"numerical_ids": ["10252"]},
            "children": [["2.F.1.c-m1", "2.F.1.c-m2", "2.F.1.c-m3"]],
        },
        "2.F.1.d": {
            "title": "Transport Refrigeration",
            "alternative_codes": [
                "9634",
                "2F1d",
                "2 F 1 d",
                "2.F.1.d-10510",
                "9634-10510",
            ],
            "info": {"numerical_ids": ["9634"]},
            "children": [["2.F.1.d-m1", "2.F.1.d-m2", "2.F.1.d-m3"]],
        },
        "2.F.1.e": {
            "title": "Mobile Air-conditioning",
            "alternative_codes": [
                "10244",
                "2F1e",
                "2 F 1 e",
                "2.F.1.e-10510",
                "10244-10510",
            ],
            "info": {"numerical_ids": ["10244"]},
            "children": [["2.F.1.e-m1", "2.F.1.e-m2", "2.F.1.e-m3"]],
        },
        "2.F.1.f": {
            "title": "Stationary Air-conditioning",
            "alternative_codes": [
                "10298",
                "2F1f",
                "2 F 1 f",
                "2.F.1.f-10510",
                "10298-10510",
            ],
            "info": {"numerical_ids": ["10298"]},
            "children": [["2.F.1.f-m1", "2.F.1.f-m2", "2.F.1.f-m3"]],
        },
        "2.F.2": {
            "title": "Foam Blowing Agents",
            "alternative_codes": ["9352", "2F2", "2 F 2", "2.F.2-10510", "9352-10510"],
            "info": {"numerical_ids": ["9352"]},
            "children": [["2.F.2.a", "2.F.2.b"]],
        },
        "2.F.2.a": {
            "title": "Closed Cells",
            "alternative_codes": [
                "8642",
                "2F2a",
                "2 F 2 a",
                "2.F.2.a-10510",
                "8642-10510",
            ],
            "info": {"numerical_ids": ["8642"]},
            "children": [["2.F.2.a-m1", "2.F.2.a-m2", "2.F.2.a-m3"]],
        },
        "2.F.2.b": {
            "title": "Open Cells",
            "alternative_codes": [
                "9224",
                "2F2b",
                "2 F 2 b",
                "2.F.2.b-10510",
                "9224-10510",
            ],
            "info": {"numerical_ids": ["9224"]},
            "children": [["2.F.2.b-m1", "2.F.2.b-m2"]],
        },
        "2.F.3": {
            "title": "Fire Protection",
            "alternative_codes": ["9296", "2F3", "2 F 3", "2.F.3-10510", "9296-10510"],
            "info": {"numerical_ids": ["9296"]},
            "children": [["2.F.3-m1", "2.F.3-m2", "2.F.3-m3"]],
        },
        "2.F.4": {
            "title": "Aerosols",
            "alternative_codes": [
                "10383",
                "2F4",
                "2 F 4",
                "2.F.4-10510",
                "10383-10510",
            ],
            "info": {"numerical_ids": ["10383"]},
            "children": [["2.F.4.a", "2.F.4.b"]],
        },
        "2.F.4.a": {
            "title": "Metered Dose Inhalers",
            "alternative_codes": [
                "8519",
                "2F4a",
                "2 F 4 a",
                "2.F.4.a-10510",
                "8519-10510",
            ],
            "info": {"numerical_ids": ["8519"]},
            "children": [["2.F.4.a-m1", "2.F.4.a-m2"]],
        },
        "2.F.4.b": {
            "title": "Other",
            "alternative_codes": [
                "8379",
                "2F4b",
                "2 F 4 b",
                "2.F.4.b-10510",
                "8379-10510",
            ],
            "info": {"numerical_ids": ["8379"]},
        },
        "2.F.5": {
            "title": "Solvents",
            "alternative_codes": ["8316", "2F5", "2 F 5", "2.F.5-10510", "8316-10510"],
            "info": {"numerical_ids": ["8316"]},
            "children": [["2.F.5-m1", "2.F.5-m2", "2.F.5-m3"]],
        },
        "2.F.6": {
            "title": "Other Applications",
            "alternative_codes": ["8607", "2F6", "2 F 6", "2.F.6-10510", "8607-10510"],
            "info": {"numerical_ids": ["8607"]},
            "children": [["2.F.6.a", "2.F.6.b"]],
        },
        "2.F.6.a": {
            "title": "Emissive",
            "alternative_codes": [
                "10246",
                "2F6a",
                "2 F 6 a",
                "2.F.6.a-10510",
                "10246-10510",
            ],
            "info": {"numerical_ids": ["10246"]},
            "children": [["2.F.6.a-m1", "2.F.6.a-m2"]],
        },
        "2.F.6.b": {
            "title": "Contained",
            "alternative_codes": [
                "10042",
                "2F6b",
                "2 F 6 b",
                "2.F.6.b-10510",
                "10042-10510",
            ],
            "info": {"numerical_ids": ["10042"]},
            "children": [["2.F.6.b-m1", "2.F.6.b-m2", "2.F.6.b-m3"]],
        },
        "2.G": {
            "title": "Other Product Manufacture and Use",
            "alternative_codes": ["8201", "2G", "2 G", "2.G-10510", "8201-10510"],
            "info": {"numerical_ids": ["8201"]},
            "children": [["2.G.1", "2.G.2", "2.G.3", "2.G.4"]],
        },
        "2.G.1": {
            "title": "Electrical Equipment",
            "alternative_codes": ["9490", "2G1", "2 G 1", "2.G.1-10510", "9490-10510"],
            "info": {"numerical_ids": ["9490"]},
            "children": [["2.G.1-m1", "2.G.1-m2", "2.G.1-m3"]],
        },
        "2.G.2": {
            "title": "SF₆ and PFCs from Other Product Use",
            "alternative_codes": [
                "10301",
                "2G2",
                "2 G 2",
                "2.G.2-10510",
                "10301-10510",
            ],
            "info": {"numerical_ids": ["10301"]},
            "children": [["2.G.2.a", "2.G.2.b", "2.G.2.c", "2.G.2.d", "2.G.2.e"]],
        },
        "2.G.2.a": {
            "title": "Military Applications",
            "alternative_codes": [
                "9055",
                "2G2a",
                "2 G 2 a",
                "2.G.2.a-10510",
                "9055-10510",
            ],
            "info": {"numerical_ids": ["9055"]},
            "children": [["2.G.2.a-m1", "2.G.2.a-m2", "2.G.2.a-m3"]],
        },
        "2.G.2.b": {
            "title": "Accelerators",
            "alternative_codes": [
                "9925",
                "2G2b",
                "2 G 2 b",
                "2.G.2.b-10510",
                "9925-10510",
            ],
            "info": {"numerical_ids": ["9925"]},
            "children": [["2.G.2.b-m1", "2.G.2.b-m2", "2.G.2.b-m3"]],
        },
        "2.G.2.c": {
            "title": "Soundproof Windows",
            "alternative_codes": [
                "9789",
                "2G2c",
                "2 G 2 c",
                "2.G.2.c-10510",
                "9789-10510",
            ],
            "info": {"numerical_ids": ["9789"]},
            "children": [["2.G.2.c-m1", "2.G.2.c-m2", "2.G.2.c-m3"]],
        },
        "2.G.2.d": {
            "title": "Adiabatic Properties: Shoes and Tyres",
            "alternative_codes": [
                "9610",
                "2G2d",
                "2 G 2 d",
                "2.G.2.d-10510",
                "9610-10510",
            ],
            "info": {"numerical_ids": ["9610"]},
            "children": [["2.G.2.d-m1", "2.G.2.d-m2", "2.G.2.d-m3"]],
        },
        "2.G.2.e": {
            "title": "Other",
            "alternative_codes": [
                "8978",
                "2G2e",
                "2 G 2 e",
                "2.G.2.e-10510",
                "8978-10510",
            ],
            "info": {"numerical_ids": ["8978"]},
        },
        "2.G.3": {
            "title": "N₂O from Product Uses",
            "alternative_codes": [
                "10433",
                "2G3",
                "2 G 3",
                "2.G.3-10510",
                "10433-10510",
            ],
            "info": {"numerical_ids": ["10433"]},
            "children": [["2.G.3.a", "2.G.3.b"]],
        },
        "2.G.3.a": {
            "title": "Medical Applications",
            "alternative_codes": [
                "8737",
                "2G3a",
                "2 G 3 a",
                "2.G.3.a-10510",
                "8737-10510",
            ],
            "info": {"numerical_ids": ["8737"]},
        },
        "2.G.3.b": {
            "title": "Other",
            "alternative_codes": [
                "9014",
                "2G3b",
                "2 G 3 b",
                "2.G.3.b-10510",
                "9014-10510",
            ],
            "info": {"numerical_ids": ["9014"]},
            "children": [["2.G.3.b.i", "2.G.3.b.ii"]],
        },
        "2.G.3.b.i": {
            "title": "Propellant for Pressure and Aerosol Products",
            "alternative_codes": [
                "9201",
                "2G3bi",
                "2 G 3 b i",
                "2.G.3.b.i-10510",
                "9201-10510",
            ],
            "info": {"numerical_ids": ["9201"]},
        },
        "2.G.3.b.ii": {
            "title": "Other",
            "alternative_codes": [
                "8566",
                "2G3bii",
                "2 G 3 b ii",
                "2.G.3.b.ii-10510",
                "8566-10510",
            ],
            "info": {"numerical_ids": ["8566"]},
        },
        "2.G.4": {
            "title": "Other",
            "alternative_codes": ["8534", "2G4", "2 G 4", "2.G.4-10510", "8534-10510"],
            "info": {"numerical_ids": ["8534"]},
        },
        "2.H": {
            "title": "Other",
            "alternative_codes": ["9899", "2H", "2 H", "2.H-10510", "9899-10510"],
            "info": {"numerical_ids": ["9899"]},
            "children": [["2.H.1", "2.H.2", "2.H.3"]],
        },
        "2.H.1": {
            "title": "Pulp and Paper",
            "alternative_codes": ["8644", "2H1", "2 H 1", "2.H.1-10510", "8644-10510"],
            "info": {"numerical_ids": ["8644"]},
            "children": [["2.H.1-m1", "2.H.1-m2", "2.H.1-m3"]],
        },
        "2.H.2": {
            "title": "Food and Beverages Industry",
            "alternative_codes": ["8797", "2H2", "2 H 2", "2.H.2-10510", "8797-10510"],
            "info": {"numerical_ids": ["8797"]},
            "children": [["2.H.2-m1", "2.H.2-m2", "2.H.2-m3"]],
        },
        "2.H.3": {
            "title": "Other",
            "alternative_codes": ["8883", "2H3", "2 H 3", "2.H.3-10510", "8883-10510"],
            "info": {"numerical_ids": ["8883"]},
        },
        "3": {
            "title": "Agriculture",
            "alternative_codes": [
                "3.",
                "10483",
                "10096",
                "3-10510",
                "10483-10510",
                "10096-10510",
            ],
            "info": {"numerical_ids": ["10483", "10096"]},
            "children": [
                ["3.A", "3.B", "3.C", "3.D", "3.E", "3.F", "3.G", "3.H", "3.I", "3.J"]
            ],
        },
        "3.A": {
            "title": "Enteric Fermentation",
            "alternative_codes": ["9559", "3A", "3 A", "3.A-10510", "9559-10510"],
            "info": {"numerical_ids": ["9559"]},
            "children": [
                [
                    "3.A-1",
                    "3.A-10",
                    "3.A-11",
                    "3.A-12",
                    "3.A-13",
                    "3.A-14",
                    "3.A-15",
                    "3.A-16",
                    "3.A-17",
                    "3.A-18",
                    "3.A-19",
                    "3.A-2",
                    "3.A-20",
                    "3.A-21",
                    "3.A-3",
                    "3.A-4",
                    "3.A-5",
                    "3.A-6",
                    "3.A-7",
                    "3.A-8",
                    "3.A-9",
                ]
            ],
        },
        "3.B": {
            "title": "Manure Management",
            "alternative_codes": ["9608", "3B", "3 B", "3.B-10510", "9608-10510"],
            "info": {"numerical_ids": ["9608"]},
            "children": [
                [
                    "3.B-1",
                    "3.B-10",
                    "3.B-11",
                    "3.B-12",
                    "3.B-13",
                    "3.B-14",
                    "3.B-15",
                    "3.B-16",
                    "3.B-17",
                    "3.B-18",
                    "3.B-19",
                    "3.B-2",
                    "3.B-20",
                    "3.B-21",
                    "3.B-3",
                    "3.B-4",
                    "3.B-5",
                    "3.B-6",
                    "3.B-7",
                    "3.B-8",
                    "3.B-9",
                ]
            ],
        },
        "3.C": {
            "title": "Rice Cultivation",
            "alternative_codes": ["10228", "3C", "3 C", "3.C-10510", "10228-10510"],
            "info": {"numerical_ids": ["10228"]},
            "children": [["3.C.1", "3.C.2", "3.C.3", "3.C.4"]],
        },
        "3.C.1": {
            "title": "Irrigated",
            "alternative_codes": ["9960", "3C1", "3 C 1", "3.C.1-10510", "9960-10510"],
            "info": {"numerical_ids": ["9960"]},
            "children": [["3.C.1.a", "3.C.1.b"]],
        },
        "3.C.1.a": {
            "title": "Continuously Flooded",
            "alternative_codes": [
                "10315",
                "3C1a",
                "3 C 1 a",
                "3.C.1.a-10510",
                "10315-10510",
            ],
            "info": {"numerical_ids": ["10315"]},
        },
        "3.C.1.b": {
            "title": "Intermittently Flooded",
            "alternative_codes": [
                "8915",
                "3C1b",
                "3 C 1 b",
                "3.C.1.b-10510",
                "8915-10510",
            ],
            "info": {"numerical_ids": ["8915"]},
            "children": [["3.C.1.b.i", "3.C.1.b.ii"]],
        },
        "3.C.1.b.i": {
            "title": "Single Aeration",
            "alternative_codes": [
                "9184",
                "3C1bi",
                "3 C 1 b i",
                "3.C.1.b.i-10510",
                "9184-10510",
            ],
            "info": {"numerical_ids": ["9184"]},
        },
        "3.C.1.b.ii": {
            "title": "Multiple Aeration",
            "alternative_codes": [
                "10065",
                "3C1bii",
                "3 C 1 b ii",
                "3.C.1.b.ii-10510",
                "10065-10510",
            ],
            "info": {"numerical_ids": ["10065"]},
        },
        "3.C.2": {
            "title": "Rainfed",
            "alternative_codes": ["8984", "3C2", "3 C 2", "3.C.2-10510", "8984-10510"],
            "info": {"numerical_ids": ["8984"]},
            "children": [["3.C.2.a", "3.C.2.b"]],
        },
        "3.C.2.a": {
            "title": "Flood Prone",
            "alternative_codes": [
                "9942",
                "3C2a",
                "3 C 2 a",
                "3.C.2.a-10510",
                "9942-10510",
            ],
            "info": {"numerical_ids": ["9942"]},
        },
        "3.C.2.b": {
            "title": "Drought Prone",
            "alternative_codes": [
                "8941",
                "3C2b",
                "3 C 2 b",
                "3.C.2.b-10510",
                "8941-10510",
            ],
            "info": {"numerical_ids": ["8941"]},
        },
        "3.C.3": {
            "title": "Deep Water",
            "alternative_codes": ["9094", "3C3", "3 C 3", "3.C.3-10510", "9094-10510"],
            "info": {"numerical_ids": ["9094"]},
            "children": [["3.C.3.a", "3.C.3.b"]],
        },
        "3.C.3.a": {
            "title": "Water Depth 50-100 cm",
            "alternative_codes": [
                "8995",
                "3C3a",
                "3 C 3 a",
                "3.C.3.a-10510",
                "8995-10510",
            ],
            "info": {"numerical_ids": ["8995"]},
        },
        "3.C.3.b": {
            "title": "Water Depth > 100 cm",
            "alternative_codes": [
                "8373",
                "3C3b",
                "3 C 3 b",
                "3.C.3.b-10510",
                "8373-10510",
            ],
            "info": {"numerical_ids": ["8373"]},
        },
        "3.C.4": {
            "title": "Other",
            "alternative_codes": ["8747", "3C4", "3 C 4", "3.C.4-10510", "8747-10510"],
            "info": {"numerical_ids": ["8747"]},
        },
        "3.D": {
            "title": "Agricultural Soils",
            "alternative_codes": ["9678", "3D", "3 D", "3.D-10510", "9678-10510"],
            "info": {"numerical_ids": ["9678"]},
            "children": [["3.D.1", "3.D.2"]],
        },
        "3.D.1": {
            "title": "Direct N₂O Emissions From Managed Soils",
            "alternative_codes": ["9087", "3D1", "3 D 1", "3.D.1-10510", "9087-10510"],
            "info": {"numerical_ids": ["9087"]},
            "children": [
                [
                    "3.D.1.a",
                    "3.D.1.b",
                    "3.D.1.c",
                    "3.D.1.d",
                    "3.D.1.e",
                    "3.D.1.f",
                    "3.D.1.g",
                ]
            ],
        },
        "3.D.1.a": {
            "title": "Inorganic N Fertilizers",
            "alternative_codes": [
                "9566",
                "3D1a",
                "3 D 1 a",
                "3.D.1.a-10510",
                "9566-10510",
            ],
            "info": {"numerical_ids": ["9566"]},
        },
        "3.D.1.b": {
            "title": "Organic N Fertilizers",
            "alternative_codes": [
                "9523",
                "3D1b",
                "3 D 1 b",
                "3.D.1.b-10510",
                "9523-10510",
            ],
            "info": {"numerical_ids": ["9523"]},
            "children": [["3.D.1.b.i", "3.D.1.b.ii", "3.D.1.b.iii"]],
        },
        "3.D.1.b.i": {
            "title": "Animal Manure Applied to Soils",
            "alternative_codes": [
                "8365",
                "3D1bi",
                "3 D 1 b i",
                "3.D.1.b.i-10510",
                "8365-10510",
            ],
            "info": {"numerical_ids": ["8365"]},
        },
        "3.D.1.b.ii": {
            "title": "Sewage Sludge Applied to Soils",
            "alternative_codes": [
                "8482",
                "3D1bii",
                "3 D 1 b ii",
                "3.D.1.b.ii-10510",
                "8482-10510",
            ],
            "info": {"numerical_ids": ["8482"]},
        },
        "3.D.1.b.iii": {
            "title": "Other Organic Fertilizers Applied to Soils",
            "alternative_codes": [
                "8218",
                "3D1biii",
                "3 D 1 b iii",
                "3.D.1.b.iii-10510",
                "8218-10510",
            ],
            "info": {"numerical_ids": ["8218"]},
        },
        "3.D.1.c": {
            "title": "Urine and Dung Deposited by Grazing Animals",
            "alternative_codes": [
                "9041",
                "3D1c",
                "3 D 1 c",
                "3.D.1.c-10510",
                "9041-10510",
            ],
            "info": {"numerical_ids": ["9041"]},
        },
        "3.D.1.d": {
            "title": "Crop Residues",
            "alternative_codes": [
                "10142",
                "3D1d",
                "3 D 1 d",
                "3.D.1.d-10510",
                "10142-10510",
            ],
            "info": {"numerical_ids": ["10142"]},
        },
        "3.D.1.e": {
            "title": "Mineralization/Immobilization Associated with Loss/Gain of Soil Organic Matter",
            "alternative_codes": [
                "9302",
                "3D1e",
                "3 D 1 e",
                "3.D.1.e-10510",
                "9302-10510",
            ],
            "info": {"numerical_ids": ["9302"]},
        },
        "3.D.1.f": {
            "title": "Cultivation of Organic Soils",
            "alternative_codes": [
                "10437",
                "3D1f",
                "3 D 1 f",
                "3.D.1.f-10510",
                "10437-10510",
            ],
            "info": {"numerical_ids": ["10437"]},
        },
        "3.D.1.g": {
            "title": "Other",
            "alternative_codes": [
                "8502",
                "3D1g",
                "3 D 1 g",
                "3.D.1.g-10510",
                "8502-10510",
            ],
            "info": {"numerical_ids": ["8502"]},
        },
        "3.D.2": {
            "title": "Indirect N₂O Emissions From Managed Soils",
            "alternative_codes": ["8920", "3D2", "3 D 2", "3.D.2-10510", "8920-10510"],
            "info": {"numerical_ids": ["8920"]},
            "children": [["3.D.2.a", "3.D.2.b"]],
        },
        "3.D.2.a": {
            "title": "Atmospheric Deposition",
            "alternative_codes": [
                "9821",
                "3D2a",
                "3 D 2 a",
                "3.D.2.a-10510",
                "9821-10510",
            ],
            "info": {"numerical_ids": ["9821"]},
        },
        "3.D.2.b": {
            "title": "Nitrogen Leaching and Run-off",
            "alternative_codes": [
                "9875",
                "3D2b",
                "3 D 2 b",
                "3.D.2.b-10510",
                "9875-10510",
            ],
            "info": {"numerical_ids": ["9875"]},
        },
        "3.E": {
            "title": "Prescribed Burning of Savannas",
            "alternative_codes": ["10322", "3E", "3 E", "3.E-10510", "10322-10510"],
            "info": {"numerical_ids": ["10322"]},
            "children": [["3.E.1", "3.E.2"]],
        },
        "3.E.1": {
            "title": "Forest Land",
            "alternative_codes": ["9488", "3E1", "3 E 1", "3.E.1-10510", "9488-10510"],
            "info": {"numerical_ids": ["9488"]},
        },
        "3.E.2": {
            "title": "Grassland",
            "alternative_codes": ["9970", "3E2", "3 E 2", "3.E.2-10510", "9970-10510"],
            "info": {"numerical_ids": ["9970"]},
        },
        "3.F": {
            "title": "Field Burning of Agricultural Residues",
            "alternative_codes": ["8783", "3F", "3 F", "3.F-10510", "8783-10510"],
            "info": {"numerical_ids": ["8783"]},
            "children": [["3.F.1", "3.F.2", "3.F.3", "3.F.4", "3.F.5"]],
        },
        "3.F.1": {
            "title": "Cereals",
            "alternative_codes": [
                "10305",
                "3F1",
                "3 F 1",
                "3.F.1-10510",
                "10305-10510",
            ],
            "info": {"numerical_ids": ["10305"]},
            "children": [["3.F.1.a", "3.F.1.b", "3.F.1.c", "3.F.1.d"]],
        },
        "3.F.1.a": {
            "title": "Wheat",
            "alternative_codes": [
                "8669",
                "3F1a",
                "3 F 1 a",
                "3.F.1.a-10510",
                "8669-10510",
            ],
            "info": {"numerical_ids": ["8669"]},
        },
        "3.F.1.b": {
            "title": "Barley",
            "alternative_codes": [
                "10193",
                "3F1b",
                "3 F 1 b",
                "3.F.1.b-10510",
                "10193-10510",
            ],
            "info": {"numerical_ids": ["10193"]},
        },
        "3.F.1.c": {
            "title": "Maize",
            "alternative_codes": [
                "8990",
                "3F1c",
                "3 F 1 c",
                "3.F.1.c-10510",
                "8990-10510",
            ],
            "info": {"numerical_ids": ["8990"]},
        },
        "3.F.1.d": {
            "title": "Other",
            "alternative_codes": [
                "9507",
                "3F1d",
                "3 F 1 d",
                "3.F.1.d-10510",
                "9507-10510",
            ],
            "info": {"numerical_ids": ["9507"]},
        },
        "3.F.2": {
            "title": "Pulses",
            "alternative_codes": ["9749", "3F2", "3 F 2", "3.F.2-10510", "9749-10510"],
            "info": {"numerical_ids": ["9749"]},
        },
        "3.F.3": {
            "title": "Tubers and Roots",
            "alternative_codes": ["9142", "3F3", "3 F 3", "3.F.3-10510", "9142-10510"],
            "info": {"numerical_ids": ["9142"]},
        },
        "3.F.4": {
            "title": "Sugar Cane",
            "alternative_codes": [
                "10387",
                "3F4",
                "3 F 4",
                "3.F.4-10510",
                "10387-10510",
            ],
            "info": {"numerical_ids": ["10387"]},
        },
        "3.F.5": {
            "title": "Other",
            "alternative_codes": [
                "10336",
                "3F5",
                "3 F 5",
                "3.F.5-10510",
                "10336-10510",
            ],
            "info": {"numerical_ids": ["10336"]},
        },
        "3.G": {
            "title": "Liming",
            "alternative_codes": ["8278", "3G", "3 G", "3.G-10510", "8278-10510"],
            "info": {"numerical_ids": ["8278"]},
            "children": [["3.G.1", "3.G.2"]],
        },
        "3.G.1": {
            "title": "Limestone CaCO₃",
            "alternative_codes": ["8504", "3G1", "3 G 1", "3.G.1-10510", "8504-10510"],
            "info": {"numerical_ids": ["8504"]},
        },
        "3.G.2": {
            "title": "Dolomite CaMg(CO₃)₂",
            "alternative_codes": ["8267", "3G2", "3 G 2", "3.G.2-10510", "8267-10510"],
            "info": {"numerical_ids": ["8267"]},
        },
        "3.H": {
            "title": "Urea Application",
            "alternative_codes": ["9927", "3H", "3 H", "3.H-10510", "9927-10510"],
            "info": {"numerical_ids": ["9927"]},
        },
        "3.I": {
            "title": "Other Carbon-containing Fertilizers",
            "alternative_codes": ["8417", "3I", "3 I", "3.I-10510", "8417-10510"],
            "info": {"numerical_ids": ["8417"]},
        },
        "3.J": {
            "title": "Other",
            "alternative_codes": ["10025", "3J", "3 J", "3.J-10510", "10025-10510"],
            "info": {"numerical_ids": ["10025"]},
        },
        "4": {
            "title": "Land Use, Land-Use Change and Forestry",
            "alternative_codes": ["4.", "9411", "4-10510", "9411-10510"],
            "info": {"numerical_ids": ["9411"]},
            "children": [
                ["4.A", "4.B", "4.C", "4.D", "4.E", "4.F", "4.G", "4.H"],
                ["4-1", "4-2", "4-3", "4-4", "4-5", "4-6"],
            ],
        },
        "4.A": {
            "title": "Forest Land",
            "alternative_codes": ["10121", "4A", "4 A", "4.A-10510", "10121-10510"],
            "info": {"numerical_ids": ["10121"]},
            "children": [
                ["4.A.1", "4.A.2"],
                [
                    "4.A-1",
                    "4.A-10",
                    "4.A-11",
                    "4.A-12",
                    "4.A-2",
                    "4.A-3",
                    "4.A-4",
                    "4.A-5",
                    "4.A-6",
                    "4.A-7",
                    "4.A-8",
                    "4.A-9",
                ],
            ],
        },
        "4.A.1": {
            "title": "Forest Land Remaining Forest Land",
            "alternative_codes": ["8348", "4A1", "4 A 1", "4.A.1-10510", "8348-10510"],
            "info": {"numerical_ids": ["8348"]},
            "children": [
                [
                    "4.A.1-1",
                    "4.A.1-2",
                    "4.A.1-3",
                    "4.A.1-4",
                    "4.A.1-5",
                    "4.A.1-6",
                    "4.A.1-7",
                    "4.A.1-8",
                ]
            ],
        },
        "4.A.2": {
            "title": "Land Converted to Forest Land",
            "alternative_codes": ["8416", "4A2", "4 A 2", "4.A.2-10510", "8416-10510"],
            "info": {"numerical_ids": ["8416"]},
            "children": [
                ["4.A.2.a", "4.A.2.b", "4.A.2.c", "4.A.2.d", "4.A.2.e"],
                [
                    "4.A.2-1",
                    "4.A.2-2",
                    "4.A.2-3",
                    "4.A.2-4",
                    "4.A.2-5",
                    "4.A.2-6",
                    "4.A.2-7",
                    "4.A.2-8",
                ],
            ],
        },
        "4.A.2.a": {
            "title": "Cropland Converted to Forest Land",
            "alternative_codes": [
                "9741",
                "4A2a",
                "4 A 2 a",
                "4.A.2.a-10510",
                "9741-10510",
            ],
            "info": {"numerical_ids": ["9741"]},
            "children": [["4.A.2.a-1", "4.A.2.a-2"]],
        },
        "4.A.2.b": {
            "title": "Grassland Converted to Forest Land",
            "alternative_codes": [
                "9851",
                "4A2b",
                "4 A 2 b",
                "4.A.2.b-10510",
                "9851-10510",
            ],
            "info": {"numerical_ids": ["9851"]},
            "children": [["4.A.2.b-1", "4.A.2.b-2"]],
        },
        "4.A.2.c": {
            "title": "Wetlands Converted to Forest Land",
            "alternative_codes": [
                "9306",
                "4A2c",
                "4 A 2 c",
                "4.A.2.c-10510",
                "9306-10510",
            ],
            "info": {"numerical_ids": ["9306"]},
            "children": [["4.A.2.c-1", "4.A.2.c-2"]],
        },
        "4.A.2.d": {
            "title": "Settlements Converted to Forest Land",
            "alternative_codes": [
                "10297",
                "4A2d",
                "4 A 2 d",
                "4.A.2.d-10510",
                "10297-10510",
            ],
            "info": {"numerical_ids": ["10297"]},
            "children": [["4.A.2.d-1", "4.A.2.d-2"]],
        },
        "4.A.2.e": {
            "title": "Other Land Converted to Forest Land",
            "alternative_codes": [
                "8735",
                "4A2e",
                "4 A 2 e",
                "4.A.2.e-10510",
                "8735-10510",
            ],
            "info": {"numerical_ids": ["8735"]},
            "children": [["4.A.2.e-1", "4.A.2.e-2"]],
        },
        "4.B": {
            "title": "Cropland",
            "alternative_codes": ["9805", "4B", "4 B", "4.B-10510", "9805-10510"],
            "info": {"numerical_ids": ["9805"]},
            "children": [
                ["4.B.1", "4.B.2"],
                [
                    "4.B-1",
                    "4.B-10",
                    "4.B-11",
                    "4.B-2",
                    "4.B-3",
                    "4.B-4",
                    "4.B-5",
                    "4.B-6",
                    "4.B-7",
                    "4.B-8",
                    "4.B-9",
                ],
            ],
        },
        "4.B.1": {
            "title": "Cropland Remaining Cropland",
            "alternative_codes": [
                "10430",
                "4B1",
                "4 B 1",
                "4.B.1-10510",
                "10430-10510",
            ],
            "info": {"numerical_ids": ["10430"]},
            "children": [["4.B.1-1", "4.B.1-2", "4.B.1-3", "4.B.1-4"]],
        },
        "4.B.2": {
            "title": "Land Converted to Cropland",
            "alternative_codes": ["8678", "4B2", "4 B 2", "4.B.2-10510", "8678-10510"],
            "info": {"numerical_ids": ["8678"]},
            "children": [
                ["4.B.2.a", "4.B.2.b", "4.B.2.c", "4.B.2.d", "4.B.2.e"],
                ["4.B.2-1", "4.B.2-2", "4.B.2-3", "4.B.2-4", "4.B.2-5"],
            ],
        },
        "4.B.2.a": {
            "title": "Forest Land Converted to Cropland",
            "alternative_codes": [
                "9799",
                "4B2a",
                "4 B 2 a",
                "4.B.2.a-10510",
                "9799-10510",
            ],
            "info": {"numerical_ids": ["9799"]},
            "children": [["4.B.2.a-1", "4.B.2.a-2"]],
        },
        "4.B.2.b": {
            "title": "Grassland Converted to Cropland",
            "alternative_codes": [
                "9491",
                "4B2b",
                "4 B 2 b",
                "4.B.2.b-10510",
                "9491-10510",
            ],
            "info": {"numerical_ids": ["9491"]},
            "children": [["4.B.2.b-1", "4.B.2.b-2"]],
        },
        "4.B.2.c": {
            "title": "Wetlands Converted to Cropland",
            "alternative_codes": [
                "10450",
                "4B2c",
                "4 B 2 c",
                "4.B.2.c-10510",
                "10450-10510",
            ],
            "info": {"numerical_ids": ["10450"]},
            "children": [["4.B.2.c-1", "4.B.2.c-2"]],
        },
        "4.B.2.d": {
            "title": "Settlements Converted to Cropland",
            "alternative_codes": [
                "8709",
                "4B2d",
                "4 B 2 d",
                "4.B.2.d-10510",
                "8709-10510",
            ],
            "info": {"numerical_ids": ["8709"]},
            "children": [["4.B.2.d-1", "4.B.2.d-2"]],
        },
        "4.B.2.e": {
            "title": "Other Land Converted to Cropland",
            "alternative_codes": [
                "9560",
                "4B2e",
                "4 B 2 e",
                "4.B.2.e-10510",
                "9560-10510",
            ],
            "info": {"numerical_ids": ["9560"]},
            "children": [["4.B.2.e-1", "4.B.2.e-2"]],
        },
        "4.C": {
            "title": "Grassland",
            "alternative_codes": ["8849", "4C", "4 C", "4.C-10510", "8849-10510"],
            "info": {"numerical_ids": ["8849"]},
            "children": [
                ["4.C.1", "4.C.2"],
                [
                    "4.C-1",
                    "4.C-10",
                    "4.C-11",
                    "4.C-2",
                    "4.C-3",
                    "4.C-4",
                    "4.C-5",
                    "4.C-6",
                    "4.C-7",
                    "4.C-8",
                    "4.C-9",
                ],
            ],
        },
        "4.C.1": {
            "title": "Grassland Remaining Grassland",
            "alternative_codes": ["9360", "4C1", "4 C 1", "4.C.1-10510", "9360-10510"],
            "info": {"numerical_ids": ["9360"]},
            "children": [["4.C.1-1", "4.C.1-2", "4.C.1-3", "4.C.1-4", "4.C.1-5"]],
        },
        "4.C.2": {
            "title": "Land Converted to Grassland",
            "alternative_codes": ["8259", "4C2", "4 C 2", "4.C.2-10510", "8259-10510"],
            "info": {"numerical_ids": ["8259"]},
            "children": [
                ["4.C.2.a", "4.C.2.b", "4.C.2.c", "4.C.2.d", "4.C.2.e"],
                ["4.C.2-1", "4.C.2-2", "4.C.2-3", "4.C.2-4", "4.C.2-5"],
            ],
        },
        "4.C.2.a": {
            "title": "Forest Land Converted to Grassland",
            "alternative_codes": [
                "9405",
                "4C2a",
                "4 C 2 a",
                "4.C.2.a-10510",
                "9405-10510",
            ],
            "info": {"numerical_ids": ["9405"]},
            "children": [["4.C.2.a-1", "4.C.2.a-2"]],
        },
        "4.C.2.b": {
            "title": "Cropland Converted to Grassland",
            "alternative_codes": [
                "9966",
                "4C2b",
                "4 C 2 b",
                "4.C.2.b-10510",
                "9966-10510",
            ],
            "info": {"numerical_ids": ["9966"]},
            "children": [["4.C.2.b-1", "4.C.2.b-2"]],
        },
        "4.C.2.c": {
            "title": "Wetlands Converted to Grassland",
            "alternative_codes": [
                "10323",
                "4C2c",
                "4 C 2 c",
                "4.C.2.c-10510",
                "10323-10510",
            ],
            "info": {"numerical_ids": ["10323"]},
            "children": [["4.C.2.c-1", "4.C.2.c-2"]],
        },
        "4.C.2.d": {
            "title": "Settlements Converted to Grassland",
            "alternative_codes": [
                "9444",
                "4C2d",
                "4 C 2 d",
                "4.C.2.d-10510",
                "9444-10510",
            ],
            "info": {"numerical_ids": ["9444"]},
            "children": [["4.C.2.d-1", "4.C.2.d-2"]],
        },
        "4.C.2.e": {
            "title": "Other Land Converted to Grassland",
            "alternative_codes": [
                "10189",
                "4C2e",
                "4 C 2 e",
                "4.C.2.e-10510",
                "10189-10510",
            ],
            "info": {"numerical_ids": ["10189"]},
            "children": [["4.C.2.e-1", "4.C.2.e-2"]],
        },
        "4.D": {
            "title": "Wetlands",
            "alternative_codes": ["9897", "4D", "4 D", "4.D-10510", "9897-10510"],
            "info": {"numerical_ids": ["9897"]},
            "children": [
                ["4.D.1", "4.D.2"],
                ["4.D-1", "4.D-2", "4.D-3", "4.D-4", "4.D-5"],
            ],
        },
        "4.D.1": {
            "title": "Wetlands Remaining Wetlands",
            "alternative_codes": ["9154", "4D1", "4 D 1", "4.D.1-10510", "9154-10510"],
            "info": {"numerical_ids": ["9154"]},
            "children": [
                ["4.D.1.a", "4.D.1.b", "4.D.1.c"],
                [
                    "4.D.1-1",
                    "4.D.1-2",
                    "4.D.1-3",
                    "4.D.1-4",
                    "4.D.1-5",
                    "4.D.1-6",
                    "4.D.1-7",
                    "4.D.1-8",
                ],
            ],
        },
        "4.D.1.a": {
            "title": "Peat Extraction Remaining Peat Extraction",
            "alternative_codes": [
                "10156",
                "4D1a",
                "4 D 1 a",
                "4.D.1.a-10510",
                "10156-10510",
            ],
            "info": {"numerical_ids": ["10156"]},
            "children": [["4.D.1.a-1"]],
        },
        "4.D.1.b": {
            "title": "Flooded Land Remaining Flooded Land",
            "alternative_codes": [
                "9151",
                "4D1b",
                "4 D 1 b",
                "4.D.1.b-10510",
                "9151-10510",
            ],
            "info": {"numerical_ids": ["9151"]},
            "children": [["4.D.1.b-1"]],
        },
        "4.D.1.c": {
            "title": "Other Wetlands Remaining Other Wetlands",
            "alternative_codes": [
                "8307",
                "4D1c",
                "4 D 1 c",
                "4.D.1.c-10510",
                "8307-10510",
            ],
            "info": {"numerical_ids": ["8307"]},
            "children": [["4.D.1.c-1"]],
        },
        "4.D.2": {
            "title": "Land Converted to Wetlands",
            "alternative_codes": ["8232", "4D2", "4 D 2", "4.D.2-10510", "8232-10510"],
            "info": {"numerical_ids": ["8232"]},
            "children": [
                ["4.D.2.a", "4.D.2.b", "4.D.2.c"],
                [
                    "4.D.2-1",
                    "4.D.2-2",
                    "4.D.2-3",
                    "4.D.2-4",
                    "4.D.2-5",
                    "4.D.2-6",
                    "4.D.2-7",
                    "4.D.2-8",
                ],
            ],
        },
        "4.D.2.a": {
            "title": "Land Converted to Peat Extraction",
            "alternative_codes": ["11002", "4D2a", "4 D 2 a"],
            "info": {"numerical_ids": ["11002"]},
            "children": [["4.D.2.a-1"]],
        },
        "4.D.2.b": {
            "title": "Land Converted to Flooded Land",
            "alternative_codes": ["11003", "4D2b", "4 D 2 b"],
            "info": {"numerical_ids": ["11003"]},
            "children": [
                ["4.D.2.b.i", "4.D.2.b.ii", "4.D.2.b.iii", "4.D.2.b.iv", "4.D.2.b.v"],
                ["4.D.2.b-1"],
            ],
        },
        "4.D.2.b.i": {
            "title": "Forest Land Converted to Flooded Land",
            "alternative_codes": ["11004", "4D2bi", "4 D 2 b i"],
            "info": {"numerical_ids": ["11004"]},
            "children": [["4.D.2.b.i-1"]],
        },
        "4.D.2.b.ii": {
            "title": "Cropland Converted to Flooded Land",
            "alternative_codes": ["11005", "4D2bii", "4 D 2 b ii"],
            "info": {"numerical_ids": ["11005"]},
            "children": [["4.D.2.b.ii-1"]],
        },
        "4.D.2.b.iii": {
            "title": "Grassland Converted to Flooded Land",
            "alternative_codes": ["11006", "4D2biii", "4 D 2 b iii"],
            "info": {"numerical_ids": ["11006"]},
            "children": [["4.D.2.b.iii-1"]],
        },
        "4.D.2.b.iv": {
            "title": "Settlements Converted to Flooded Land",
            "alternative_codes": ["11007", "4D2biv", "4 D 2 b iv"],
            "info": {"numerical_ids": ["11007"]},
            "children": [["4.D.2.b.iv-1"]],
        },
        "4.D.2.b.v": {
            "title": "Other Land Converted to Flooded Land",
            "alternative_codes": ["11008", "4D2bv", "4 D 2 b v"],
            "info": {"numerical_ids": ["11008"]},
            "children": [["4.D.2.b.v-1"]],
        },
        "4.D.2.c": {
            "title": "Land Converted to Other Wetlands",
            "alternative_codes": ["11009", "4D2c", "4 D 2 c"],
            "info": {"numerical_ids": ["11009"]},
            "children": [
                ["4.D.2.c.i", "4.D.2.c.ii", "4.D.2.c.iii", "4.D.2.c.iv", "4.D.2.c.v"],
                ["4.D.2.c-1"],
            ],
        },
        "4.D.2.c.i": {
            "title": "Forest Land Converted to Other Wetlands",
            "alternative_codes": ["11010", "4D2ci", "4 D 2 c i"],
            "info": {"numerical_ids": ["11010"]},
            "children": [["4.D.2.c.i-1", "4.D.2.c.i-2"]],
        },
        "4.D.2.c.ii": {
            "title": "Cropland Converted to Other Wetlands",
            "alternative_codes": ["11011", "4D2cii", "4 D 2 c ii"],
            "info": {"numerical_ids": ["11011"]},
            "children": [["4.D.2.c.ii-1", "4.D.2.c.ii-2"]],
        },
        "4.D.2.c.iii": {
            "title": "Grassland Converted to Other Wetlands",
            "alternative_codes": ["11012", "4D2ciii", "4 D 2 c iii"],
            "info": {"numerical_ids": ["11012"]},
            "children": [["4.D.2.c.iii-1", "4.D.2.c.iii-2"]],
        },
        "4.D.2.c.iv": {
            "title": "Settlements Converted to Other Wetlands",
            "alternative_codes": ["11013", "4D2civ", "4 D 2 c iv"],
            "info": {"numerical_ids": ["11013"]},
            "children": [["4.D.2.c.iv-1", "4.D.2.c.iv-2"]],
        },
        "4.D.2.c.v": {
            "title": "Other Land Converted to Other Wetlands",
            "alternative_codes": ["11014", "4D2cv", "4 D 2 c v"],
            "info": {"numerical_ids": ["11014"]},
            "children": [["4.D.2.c.v-1", "4.D.2.c.v-2"]],
        },
        "4.E": {
            "title": "Settlements",
            "alternative_codes": ["10314", "4E", "4 E", "4.E-10510", "10314-10510"],
            "info": {"numerical_ids": ["10314"]},
            "children": [["4.E.1", "4.E.2"], ["4.E-1", "4.E-2", "4.E-3", "4.E-4"]],
        },
        "4.E.1": {
            "title": "Settlements Remaining Settlements",
            "alternative_codes": [
                "10132",
                "4E1",
                "4 E 1",
                "4.E.1-10510",
                "10132-10510",
            ],
            "info": {"numerical_ids": ["10132"]},
            "children": [["4.E.1-1", "4.E.1-2", "4.E.1-3", "4.E.1-4", "4.E.1-5"]],
        },
        "4.E.2": {
            "title": "Land Converted to Settlements",
            "alternative_codes": ["9506", "4E2", "4 E 2", "4.E.2-10510", "9506-10510"],
            "info": {"numerical_ids": ["9506"]},
            "children": [
                ["4.E.2.a", "4.E.2.b", "4.E.2.c", "4.E.2.d", "4.E.2.e"],
                ["4.E.2-1", "4.E.2-2", "4.E.2-3", "4.E.2-4", "4.E.2-5"],
            ],
        },
        "4.E.2.a": {
            "title": "Forest Land Converted to Settlements",
            "alternative_codes": [
                "10183",
                "4E2a",
                "4 E 2 a",
                "4.E.2.a-10510",
                "10183-10510",
            ],
            "info": {"numerical_ids": ["10183"]},
            "children": [["4.E.2.a-1", "4.E.2.a-2"]],
        },
        "4.E.2.b": {
            "title": "Cropland Converted to Settlements",
            "alternative_codes": [
                "9914",
                "4E2b",
                "4 E 2 b",
                "4.E.2.b-10510",
                "9914-10510",
            ],
            "info": {"numerical_ids": ["9914"]},
            "children": [["4.E.2.b-1", "4.E.2.b-2"]],
        },
        "4.E.2.c": {
            "title": "Grassland Converted to Settlements",
            "alternative_codes": [
                "10026",
                "4E2c",
                "4 E 2 c",
                "4.E.2.c-10510",
                "10026-10510",
            ],
            "info": {"numerical_ids": ["10026"]},
            "children": [["4.E.2.c-1", "4.E.2.c-2"]],
        },
        "4.E.2.d": {
            "title": "Wetlands Converted to Settlements",
            "alternative_codes": [
                "8465",
                "4E2d",
                "4 E 2 d",
                "4.E.2.d-10510",
                "8465-10510",
            ],
            "info": {"numerical_ids": ["8465"]},
            "children": [["4.E.2.d-1", "4.E.2.d-2"]],
        },
        "4.E.2.e": {
            "title": "Other Land Converted to Settlements",
            "alternative_codes": [
                "9857",
                "4E2e",
                "4 E 2 e",
                "4.E.2.e-10510",
                "9857-10510",
            ],
            "info": {"numerical_ids": ["9857"]},
            "children": [["4.E.2.e-1", "4.E.2.e-2"]],
        },
        "4.F": {
            "title": "Other Land",
            "alternative_codes": ["8288", "4F", "4 F", "4.F-10510", "8288-10510"],
            "info": {"numerical_ids": ["8288"]},
            "children": [["4.F.1", "4.F.2"], ["4.F-1", "4.F-2", "4.F-3"]],
        },
        "4.F.1": {
            "title": "Other Land Remaining Other Land",
            "alternative_codes": ["11015", "4F1", "4 F 1"],
            "info": {"numerical_ids": ["11015"]},
            "children": [["4.F.1-1"]],
        },
        "4.F.2": {
            "title": "Land Converted to Other Land",
            "alternative_codes": ["8343", "4F2", "4 F 2", "4.F.2-10510", "8343-10510"],
            "info": {"numerical_ids": ["8343"]},
            "children": [
                ["4.F.2.a", "4.F.2.b", "4.F.2.c", "4.F.2.d", "4.F.2.e"],
                ["4.F.2-1"],
            ],
        },
        "4.F.2.a": {
            "title": "Forest Land Converted to Other Land",
            "alternative_codes": [
                "8488",
                "4F2a",
                "4 F 2 a",
                "4.F.2.a-10510",
                "8488-10510",
            ],
            "info": {"numerical_ids": ["8488"]},
            "children": [["4.F.2.a-1"]],
        },
        "4.F.2.b": {
            "title": "Cropland Converted to Other Land",
            "alternative_codes": [
                "8234",
                "4F2b",
                "4 F 2 b",
                "4.F.2.b-10510",
                "8234-10510",
            ],
            "info": {"numerical_ids": ["8234"]},
            "children": [["4.F.2.b-1"]],
        },
        "4.F.2.c": {
            "title": "Grassland Converted  to Other Land",
            "alternative_codes": [
                "8574",
                "4F2c",
                "4 F 2 c",
                "4.F.2.c-10510",
                "8574-10510",
            ],
            "info": {"numerical_ids": ["8574"]},
            "children": [["4.F.2.c-1"]],
        },
        "4.F.2.d": {
            "title": "Wetlands Converted to Other Land",
            "alternative_codes": [
                "10371",
                "4F2d",
                "4 F 2 d",
                "4.F.2.d-10510",
                "10371-10510",
            ],
            "info": {"numerical_ids": ["10371"]},
            "children": [["4.F.2.d-1"]],
        },
        "4.F.2.e": {
            "title": "Settlements Converted to Other Land",
            "alternative_codes": [
                "9019",
                "4F2e",
                "4 F 2 e",
                "4.F.2.e-10510",
                "9019-10510",
            ],
            "info": {"numerical_ids": ["9019"]},
            "children": [["4.F.2.e-1"]],
        },
        "4.G": {
            "title": "Harvested Wood Products",
            "alternative_codes": ["9133", "4G", "4 G", "4.G-10510", "9133-10510"],
            "info": {"numerical_ids": ["9133"]},
            "children": [["11035", "4.G.1", "4.G.2", "4.G.3"]],
        },
        "4.G.1": {
            "title": "Solid Wood",
            "alternative_codes": [
                "11016",
                "4G1",
                "4 G 1",
                "4.G.1-10510",
                "11016-10510",
            ],
            "info": {"numerical_ids": ["11016"]},
            "children": [["4.G.1.a", "4.G.1.b", "4.G.1.c"]],
        },
        "4.G.1.a": {
            "title": "Sawnwood",
            "alternative_codes": [
                "11017",
                "4G1a",
                "4 G 1 a",
                "4.G.1.a-10510",
                "11017-10510",
            ],
            "info": {"numerical_ids": ["11017"]},
        },
        "4.G.1.b": {
            "title": "Wood Panels",
            "alternative_codes": [
                "11018",
                "4G1b",
                "4 G 1 b",
                "4.G.1.b-10510",
                "11018-10510",
            ],
            "info": {"numerical_ids": ["11018"]},
        },
        "4.G.1.c": {
            "title": "Other Solid Wood Products",
            "alternative_codes": [
                "11019",
                "4G1c",
                "4 G 1 c",
                "4.G.1.c-10510",
                "11019-10510",
            ],
            "info": {"numerical_ids": ["11019"]},
        },
        "4.G.2": {
            "title": "Paper and Paperboard",
            "alternative_codes": [
                "11020",
                "4G2",
                "4 G 2",
                "4.G.2-10510",
                "11020-10510",
            ],
            "info": {"numerical_ids": ["11020"]},
        },
        "4.G.3": {
            "title": "Other",
            "alternative_codes": [
                "11021",
                "4G3",
                "4 G 3",
                "4.G.3-10510",
                "11021-10510",
            ],
            "info": {"numerical_ids": ["11021"]},
        },
        "4.H": {
            "title": "Other",
            "alternative_codes": ["9158", "4H", "4 H", "4.H-10510", "9158-10510"],
            "info": {"numerical_ids": ["9158"]},
            "children": [["4.H-1", "4.H-2", "4.H-3"]],
        },
        "5": {
            "title": "Waste",
            "alternative_codes": [
                "5.",
                "10484",
                "10159",
                "5-10510",
                "10484-10510",
                "10159-10510",
            ],
            "info": {"numerical_ids": ["10484", "10159"]},
            "children": [["11022", "5.A", "5.B", "5.C", "5.D", "5.E"]],
        },
        "5.A": {
            "title": "Solid Waste Disposal",
            "alternative_codes": ["9284", "5A", "5 A", "5.A-10510", "9284-10510"],
            "info": {"numerical_ids": ["9284"]},
            "children": [["5.A.1", "5.A.2", "5.A.3"]],
        },
        "5.A.1": {
            "title": "Managed Waste Disposal Sites",
            "alternative_codes": ["8477", "5A1", "5 A 1", "5.A.1-10510", "8477-10510"],
            "info": {"numerical_ids": ["8477"]},
            "children": [["5.A.1.a", "5.A.1.b"]],
        },
        "5.A.1.a": {
            "title": "Anaerobic",
            "alternative_codes": [
                "9839",
                "5A1a",
                "5 A 1 a",
                "5.A.1.a-10510",
                "9839-10510",
            ],
            "info": {"numerical_ids": ["9839"]},
        },
        "5.A.1.b": {
            "title": "Semi-aerobic",
            "alternative_codes": [
                "9144",
                "5A1b",
                "5 A 1 b",
                "5.A.1.b-10510",
                "9144-10510",
            ],
            "info": {"numerical_ids": ["9144"]},
        },
        "5.A.2": {
            "title": "Unmanaged Waste Disposal Sites",
            "alternative_codes": [
                "10235",
                "5A2",
                "5 A 2",
                "5.A.2-10510",
                "10235-10510",
            ],
            "info": {"numerical_ids": ["10235"]},
        },
        "5.A.3": {
            "title": "Uncategorized Waste Disposal Sites",
            "alternative_codes": ["8652", "5A3", "5 A 3", "5.A.3-10510", "8652-10510"],
            "info": {"numerical_ids": ["8652"]},
        },
        "5.B": {
            "title": "Biological Treatment of Solid Waste",
            "alternative_codes": ["9245", "5B", "5 B", "5.B-10510", "9245-10510"],
            "info": {"numerical_ids": ["9245"]},
            "children": [["5.B.1", "5.B.2"]],
        },
        "5.B.1": {
            "title": "Composting",
            "alternative_codes": ["8701", "5B1", "5 B 1", "5.B.1-10510", "8701-10510"],
            "info": {"numerical_ids": ["8701"]},
            "children": [["5.B.1.a", "5.B.1.b"]],
        },
        "5.B.1.a": {
            "title": "Municipal Solid Waste",
            "alternative_codes": [
                "9682",
                "5B1a",
                "5 B 1 a",
                "5.B.1.a-10510",
                "9682-10510",
            ],
            "info": {"numerical_ids": ["9682"]},
        },
        "5.B.1.b": {
            "title": "Other",
            "alternative_codes": [
                "8640",
                "5B1b",
                "5 B 1 b",
                "5.B.1.b-10510",
                "8640-10510",
            ],
            "info": {"numerical_ids": ["8640"]},
        },
        "5.B.2": {
            "title": "Anaerobic Digestion at Biogas Facilities",
            "alternative_codes": ["8225", "5B2", "5 B 2", "5.B.2-10510", "8225-10510"],
            "info": {"numerical_ids": ["8225"]},
            "children": [["5.B.2.a", "5.B.2.b"]],
        },
        "5.B.2.a": {
            "title": "Municipal Solid Waste",
            "alternative_codes": [
                "9290",
                "5B2a",
                "5 B 2 a",
                "5.B.2.a-10510",
                "9290-10510",
            ],
            "info": {"numerical_ids": ["9290"]},
        },
        "5.B.2.b": {
            "title": "Other",
            "alternative_codes": [
                "9639",
                "5B2b",
                "5 B 2 b",
                "5.B.2.b-10510",
                "9639-10510",
            ],
            "info": {"numerical_ids": ["9639"]},
        },
        "5.C": {
            "title": "Incineration and Open Burning of Waste",
            "alternative_codes": ["8227", "5C", "5 C", "5.C-10510", "8227-10510"],
            "info": {"numerical_ids": ["8227"]},
            "children": [["5.C.1", "5.C.2"]],
        },
        "5.C.1": {
            "title": "Waste Incineration",
            "alternative_codes": [
                "10408",
                "5C1",
                "5 C 1",
                "5.C.1-10510",
                "10408-10510",
            ],
            "info": {"numerical_ids": ["10408"]},
            "children": [["5.C.1.a", "5.C.1.b"]],
        },
        "5.C.1.a": {
            "title": "Biogenic",
            "alternative_codes": [
                "8776",
                "5C1a",
                "5 C 1 a",
                "5.C.1.a-10510",
                "8776-10510",
            ],
            "info": {"numerical_ids": ["8776"]},
            "children": [["5.C.1.a.i", "5.C.1.a.ii"]],
        },
        "5.C.1.a.i": {
            "title": "Municipal Solid Waste",
            "alternative_codes": [
                "9069",
                "5C1ai",
                "5 C 1 a i",
                "5.C.1.a.i-10510",
                "9069-10510",
            ],
            "info": {"numerical_ids": ["9069"]},
        },
        "5.C.1.a.ii": {
            "title": "Other",
            "alternative_codes": [
                "8401",
                "5C1aii",
                "5 C 1 a ii",
                "5.C.1.a.ii-10510",
                "8401-10510",
            ],
            "info": {"numerical_ids": ["8401"]},
            "children": [
                [
                    "5.C.1.a.ii.1",
                    "5.C.1.a.ii.2",
                    "5.C.1.a.ii.3",
                    "5.C.1.a.ii.4",
                    "5.C.1.a.ii.5",
                ]
            ],
        },
        "5.C.1.a.ii.1": {
            "title": "Industrial Solid Wastes",
            "alternative_codes": [
                "8260",
                "5C1aii1",
                "5 C 1 a ii 1",
                "5.C.1.a.ii.1-10510",
                "8260-10510",
            ],
            "info": {"numerical_ids": ["8260"]},
        },
        "5.C.1.a.ii.2": {
            "title": "Hazardous Waste",
            "alternative_codes": [
                "9329",
                "5C1aii2",
                "5 C 1 a ii 2",
                "5.C.1.a.ii.2-10510",
                "9329-10510",
            ],
            "info": {"numerical_ids": ["9329"]},
        },
        "5.C.1.a.ii.3": {
            "title": "Clinical Waste",
            "alternative_codes": [
                "9141",
                "5C1aii3",
                "5 C 1 a ii 3",
                "5.C.1.a.ii.3-10510",
                "9141-10510",
            ],
            "info": {"numerical_ids": ["9141"]},
        },
        "5.C.1.a.ii.4": {
            "title": "Sewage Sludge",
            "alternative_codes": [
                "9538",
                "5C1aii4",
                "5 C 1 a ii 4",
                "5.C.1.a.ii.4-10510",
                "9538-10510",
            ],
            "info": {"numerical_ids": ["9538"]},
        },
        "5.C.1.a.ii.5": {
            "title": "Other",
            "alternative_codes": [
                "9218",
                "5C1aii5",
                "5 C 1 a ii 5",
                "5.C.1.a.ii.5-10510",
                "9218-10510",
            ],
            "info": {"numerical_ids": ["9218"]},
        },
        "5.C.1.b": {
            "title": "Non-biogenic",
            "alternative_codes": [
                "9979",
                "5C1b",
                "5 C 1 b",
                "5.C.1.b-10510",
                "9979-10510",
            ],
            "info": {"numerical_ids": ["9979"]},
            "children": [["5.C.1.b.i", "5.C.1.b.ii"]],
        },
        "5.C.1.b.i": {
            "title": "Municipal Solid Waste",
            "alternative_codes": [
                "10302",
                "5C1bi",
                "5 C 1 b i",
                "5.C.1.b.i-10510",
                "10302-10510",
            ],
            "info": {"numerical_ids": ["10302"]},
        },
        "5.C.1.b.ii": {
            "title": "Other",
            "alternative_codes": [
                "9696",
                "5C1bii",
                "5 C 1 b ii",
                "5.C.1.b.ii-10510",
                "9696-10510",
            ],
            "info": {"numerical_ids": ["9696"]},
            "children": [
                [
                    "5.C.1.b.ii.1",
                    "5.C.1.b.ii.2",
                    "5.C.1.b.ii.3",
                    "5.C.1.b.ii.4",
                    "5.C.1.b.ii.5",
                    "5.C.1.b.ii.6",
                ]
            ],
        },
        "5.C.1.b.ii.1": {
            "title": "Industrial Solid Wastes",
            "alternative_codes": [
                "8158",
                "5C1bii1",
                "5 C 1 b ii 1",
                "5.C.1.b.ii.1-10510",
                "8158-10510",
            ],
            "info": {"numerical_ids": ["8158"]},
        },
        "5.C.1.b.ii.2": {
            "title": "Hazardous Waste",
            "alternative_codes": [
                "9250",
                "5C1bii2",
                "5 C 1 b ii 2",
                "5.C.1.b.ii.2-10510",
                "9250-10510",
            ],
            "info": {"numerical_ids": ["9250"]},
        },
        "5.C.1.b.ii.3": {
            "title": "Clinical Waste",
            "alternative_codes": [
                "10050",
                "5C1bii3",
                "5 C 1 b ii 3",
                "5.C.1.b.ii.3-10510",
                "10050-10510",
            ],
            "info": {"numerical_ids": ["10050"]},
        },
        "5.C.1.b.ii.4": {
            "title": "Sewage Sludge",
            "alternative_codes": [
                "8619",
                "5C1bii4",
                "5 C 1 b ii 4",
                "5.C.1.b.ii.4-10510",
                "8619-10510",
            ],
            "info": {"numerical_ids": ["8619"]},
        },
        "5.C.1.b.ii.5": {
            "title": "Fossil Liquid Waste",
            "alternative_codes": [
                "9730",
                "5C1bii5",
                "5 C 1 b ii 5",
                "5.C.1.b.ii.5-10510",
                "9730-10510",
            ],
            "info": {"numerical_ids": ["9730"]},
        },
        "5.C.1.b.ii.6": {
            "title": "Other",
            "alternative_codes": [
                "9649",
                "5C1bii6",
                "5 C 1 b ii 6",
                "5.C.1.b.ii.6-10510",
                "9649-10510",
            ],
            "info": {"numerical_ids": ["9649"]},
        },
        "5.C.2": {
            "title": "Open Burning of Waste",
            "alternative_codes": ["8943", "5C2", "5 C 2", "5.C.2-10510", "8943-10510"],
            "info": {"numerical_ids": ["8943"]},
            "children": [["5.C.2.a", "5.C.2.b"]],
        },
        "5.C.2.a": {
            "title": "Biogenic",
            "alternative_codes": [
                "8825",
                "5C2a",
                "5 C 2 a",
                "5.C.2.a-10510",
                "8825-10510",
            ],
            "info": {"numerical_ids": ["8825"]},
            "children": [["5.C.2.a.i", "5.C.2.a.ii"]],
        },
        "5.C.2.a.i": {
            "title": "Municipal Solid Waste",
            "alternative_codes": [
                "10182",
                "5C2ai",
                "5 C 2 a i",
                "5.C.2.a.i-10510",
                "10182-10510",
            ],
            "info": {"numerical_ids": ["10182"]},
        },
        "5.C.2.a.ii": {
            "title": "Other",
            "alternative_codes": [
                "8772",
                "5C2aii",
                "5 C 2 a ii",
                "5.C.2.a.ii-10510",
                "8772-10510",
            ],
            "info": {"numerical_ids": ["8772"]},
        },
        "5.C.2.b": {
            "title": "Non-biogenic",
            "alternative_codes": [
                "8910",
                "5C2b",
                "5 C 2 b",
                "5.C.2.b-10510",
                "8910-10510",
            ],
            "info": {"numerical_ids": ["8910"]},
            "children": [["5.C.2.b.i", "5.C.2.b.ii"]],
        },
        "5.C.2.b.i": {
            "title": "Municipal Solid Waste",
            "alternative_codes": [
                "8768",
                "5C2bi",
                "5 C 2 b i",
                "5.C.2.b.i-10510",
                "8768-10510",
            ],
            "info": {"numerical_ids": ["8768"]},
        },
        "5.C.2.b.ii": {
            "title": "Other",
            "alternative_codes": [
                "9181",
                "5C2bii",
                "5 C 2 b ii",
                "5.C.2.b.ii-10510",
                "9181-10510",
            ],
            "info": {"numerical_ids": ["9181"]},
        },
        "5.D": {
            "title": "Wastewater Treatment and Discharge",
            "alternative_codes": ["8423", "5D", "5 D", "5.D-10510", "8423-10510"],
            "info": {"numerical_ids": ["8423"]},
            "children": [["5.D.1", "5.D.2", "5.D.3"]],
        },
        "5.D.1": {
            "title": "Domestic Wastewater",
            "alternative_codes": [
                "10391",
                "5D1",
                "5 D 1",
                "5.D.1-10510",
                "10391-10510",
            ],
            "info": {"numerical_ids": ["10391"]},
        },
        "5.D.2": {
            "title": "Industrial Wastewater",
            "alternative_codes": ["9831", "5D2", "5 D 2", "5.D.2-10510", "9831-10510"],
            "info": {"numerical_ids": ["9831"]},
        },
        "5.D.3": {
            "title": "Other",
            "alternative_codes": ["8153", "5D3", "5 D 3", "5.D.3-10510", "8153-10510"],
            "info": {"numerical_ids": ["8153"]},
        },
        "5.E": {
            "title": "Other",
            "alternative_codes": ["8284", "5E", "5 E", "5.E-10510", "8284-10510"],
            "info": {"numerical_ids": ["8284"]},
        },
        "6": {
            "title": "Other",
            "alternative_codes": [
                "6.",
                "10476",
                "10485",
                "6-10510",
                "10476-10510",
                "10485-10510",
            ],
            "info": {"numerical_ids": ["10476", "10485"]},
        },
        "8270-1": {"title": "Biomass", "alternative_codes": ["8270-10513"]},
        "8828-1": {"title": "Biomass", "alternative_codes": ["8828-10513"]},
        "8828-2": {"title": "Gas/Diesel Oil", "alternative_codes": ["8828-10523"]},
        "8828-3": {"title": "Gaseous Fuels", "alternative_codes": ["8828-10524"]},
        "8828-4": {"title": "Gasoline", "alternative_codes": ["8828-10525"]},
        "8828-5": {"title": "Other Fossil Fuels", "alternative_codes": ["8828-10538"]},
        "8828-6": {"title": "Other Liquid Fuels", "alternative_codes": ["8828-10542"]},
        "8828-7": {"title": "Residual Fuel Oil", "alternative_codes": ["8828-10549"]},
        "10357-1": {"title": "Aviation Gasoline", "alternative_codes": ["10357-10512"]},
        "10357-2": {"title": "Biomass", "alternative_codes": ["10357-10513"]},
        "10357-3": {"title": "Jet Kerosene", "alternative_codes": ["10357-10526"]},
        "1.A.1-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1-10513", "10402-10513"],
        },
        "1.A.1-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1-10524", "10402-10524"],
        },
        "1.A.1-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1-10530", "10402-10530"],
        },
        "1.A.1-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1-10538", "10402-10538"],
        },
        "1.A.1-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1-10546", "10402-10546"],
        },
        "1.A.1-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1-10552", "10402-10552"],
        },
        "1.A.1.a-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.a-10513", "9422-10513"],
        },
        "1.A.1.a-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.a-10524", "9422-10524"],
        },
        "1.A.1.a-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.a-10530", "9422-10530"],
        },
        "1.A.1.a-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.a-10538", "9422-10538"],
        },
        "1.A.1.a-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.a-10546", "9422-10546"],
        },
        "1.A.1.a-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.a-10552", "9422-10552"],
        },
        "1.A.1.a.i-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.a.i-10513", "8616-10513"],
        },
        "1.A.1.a.i-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.a.i-10524", "8616-10524"],
        },
        "1.A.1.a.i-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.a.i-10530", "8616-10530"],
        },
        "1.A.1.a.i-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.a.i-10538", "8616-10538"],
        },
        "1.A.1.a.i-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.a.i-10546", "8616-10546"],
        },
        "1.A.1.a.i-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.a.i-10552", "8616-10552"],
        },
        "1.A.1.a.ii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.a.ii-10513", "9614-10513"],
        },
        "1.A.1.a.ii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.a.ii-10524", "9614-10524"],
        },
        "1.A.1.a.ii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.a.ii-10530", "9614-10530"],
        },
        "1.A.1.a.ii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.a.ii-10538", "9614-10538"],
        },
        "1.A.1.a.ii-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.a.ii-10546", "9614-10546"],
        },
        "1.A.1.a.ii-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.a.ii-10552", "9614-10552"],
        },
        "1.A.1.a.iii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.a.iii-10513", "9971-10513"],
        },
        "1.A.1.a.iii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.a.iii-10524", "9971-10524"],
        },
        "1.A.1.a.iii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.a.iii-10530", "9971-10530"],
        },
        "1.A.1.a.iii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.a.iii-10538", "9971-10538"],
        },
        "1.A.1.a.iii-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.a.iii-10546", "9971-10546"],
        },
        "1.A.1.a.iii-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.a.iii-10552", "9971-10552"],
        },
        "1.A.1.a.iv-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.a.iv-10513", "8368-10513"],
        },
        "1.A.1.a.iv-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.a.iv-10524", "8368-10524"],
        },
        "1.A.1.a.iv-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.a.iv-10530", "8368-10530"],
        },
        "1.A.1.a.iv-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.a.iv-10538", "8368-10538"],
        },
        "1.A.1.a.iv-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.a.iv-10546", "8368-10546"],
        },
        "1.A.1.a.iv-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.a.iv-10552", "8368-10552"],
        },
        "1.A.1.b-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.b-10513", "9771-10513"],
        },
        "1.A.1.b-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.b-10524", "9771-10524"],
        },
        "1.A.1.b-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.b-10530", "9771-10530"],
        },
        "1.A.1.b-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.b-10538", "9771-10538"],
        },
        "1.A.1.b-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.b-10546", "9771-10546"],
        },
        "1.A.1.b-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.b-10552", "9771-10552"],
        },
        "1.A.1.c-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.c-10513", "9004-10513"],
        },
        "1.A.1.c-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.c-10524", "9004-10524"],
        },
        "1.A.1.c-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.c-10530", "9004-10530"],
        },
        "1.A.1.c-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.c-10538", "9004-10538"],
        },
        "1.A.1.c-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.c-10546", "9004-10546"],
        },
        "1.A.1.c-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.c-10552", "9004-10552"],
        },
        "1.A.1.c.i-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.c.i-10513", "10306-10513"],
        },
        "1.A.1.c.i-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.c.i-10524", "10306-10524"],
        },
        "1.A.1.c.i-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.c.i-10530", "10306-10530"],
        },
        "1.A.1.c.i-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.c.i-10538", "10306-10538"],
        },
        "1.A.1.c.i-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.c.i-10546", "10306-10546"],
        },
        "1.A.1.c.i-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.c.i-10552", "10306-10552"],
        },
        "1.A.1.c.ii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.c.ii-10513", "10425-10513"],
        },
        "1.A.1.c.ii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.c.ii-10524", "10425-10524"],
        },
        "1.A.1.c.ii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.c.ii-10530", "10425-10530"],
        },
        "1.A.1.c.ii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.c.ii-10538", "10425-10538"],
        },
        "1.A.1.c.ii-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.c.ii-10546", "10425-10546"],
        },
        "1.A.1.c.ii-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.c.ii-10552", "10425-10552"],
        },
        "1.A.1.c.iii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.c.iii-10513", "8335-10513"],
        },
        "1.A.1.c.iii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.c.iii-10524", "8335-10524"],
        },
        "1.A.1.c.iii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.c.iii-10530", "8335-10530"],
        },
        "1.A.1.c.iii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.c.iii-10538", "8335-10538"],
        },
        "1.A.1.c.iii-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.c.iii-10546", "8335-10546"],
        },
        "1.A.1.c.iii-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.c.iii-10552", "8335-10552"],
        },
        "1.A.1.c.iv-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.1.c.iv-10513", "8656-10513"],
        },
        "1.A.1.c.iv-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.1.c.iv-10524", "8656-10524"],
        },
        "1.A.1.c.iv-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.1.c.iv-10530", "8656-10530"],
        },
        "1.A.1.c.iv-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.1.c.iv-10538", "8656-10538"],
        },
        "1.A.1.c.iv-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.1.c.iv-10546", "8656-10546"],
        },
        "1.A.1.c.iv-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.1.c.iv-10552", "8656-10552"],
        },
        "1.A.2-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2-10513", "8556-10513"],
        },
        "1.A.2-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2-10524", "8556-10524"],
        },
        "1.A.2-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2-10530", "8556-10530"],
        },
        "1.A.2-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2-10538", "8556-10538"],
        },
        "1.A.2-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2-10546", "8556-10546"],
        },
        "1.A.2-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2-10552", "8556-10552"],
        },
        "1.A.2.a-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.a-10513", "10329-10513"],
        },
        "1.A.2.a-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.a-10524", "10329-10524"],
        },
        "1.A.2.a-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.a-10530", "10329-10530"],
        },
        "1.A.2.a-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.a-10538", "10329-10538"],
        },
        "1.A.2.a-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.a-10546", "10329-10546"],
        },
        "1.A.2.a-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.a-10552", "10329-10552"],
        },
        "1.A.2.b-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.b-10513", "9859-10513"],
        },
        "1.A.2.b-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.b-10524", "9859-10524"],
        },
        "1.A.2.b-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.b-10530", "9859-10530"],
        },
        "1.A.2.b-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.b-10538", "9859-10538"],
        },
        "1.A.2.b-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.b-10546", "9859-10546"],
        },
        "1.A.2.b-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.b-10552", "9859-10552"],
        },
        "1.A.2.c-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.c-10513", "9369-10513"],
        },
        "1.A.2.c-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.c-10524", "9369-10524"],
        },
        "1.A.2.c-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.c-10530", "9369-10530"],
        },
        "1.A.2.c-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.c-10538", "9369-10538"],
        },
        "1.A.2.c-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.c-10546", "9369-10546"],
        },
        "1.A.2.c-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.c-10552", "9369-10552"],
        },
        "1.A.2.d-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.d-10513", "10119-10513"],
        },
        "1.A.2.d-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.d-10524", "10119-10524"],
        },
        "1.A.2.d-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.d-10530", "10119-10530"],
        },
        "1.A.2.d-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.d-10538", "10119-10538"],
        },
        "1.A.2.d-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.d-10546", "10119-10546"],
        },
        "1.A.2.d-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.d-10552", "10119-10552"],
        },
        "1.A.2.e-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.e-10513", "8321-10513"],
        },
        "1.A.2.e-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.e-10524", "8321-10524"],
        },
        "1.A.2.e-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.e-10530", "8321-10530"],
        },
        "1.A.2.e-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.e-10538", "8321-10538"],
        },
        "1.A.2.e-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.e-10546", "8321-10546"],
        },
        "1.A.2.e-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.e-10552", "8321-10552"],
        },
        "1.A.2.f-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.f-10513", "8876-10513"],
        },
        "1.A.2.f-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.f-10524", "8876-10524"],
        },
        "1.A.2.f-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.f-10530", "8876-10530"],
        },
        "1.A.2.f-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.f-10538", "8876-10538"],
        },
        "1.A.2.f-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.f-10546", "8876-10546"],
        },
        "1.A.2.f-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.f-10552", "8876-10552"],
        },
        "1.A.2.g-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.g-10513", "9832-10513"],
        },
        "1.A.2.g-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.g-10524", "9832-10524"],
        },
        "1.A.2.g-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.g-10530", "9832-10530"],
        },
        "1.A.2.g-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.g-10538", "9832-10538"],
        },
        "1.A.2.g-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.g-10546", "9832-10546"],
        },
        "1.A.2.g-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.g-10552", "9832-10552"],
        },
        "1.A.2.g.i-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.g.i-10513", "10308-10513"],
        },
        "1.A.2.g.i-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.g.i-10524", "10308-10524"],
        },
        "1.A.2.g.i-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.g.i-10530", "10308-10530"],
        },
        "1.A.2.g.i-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.g.i-10538", "10308-10538"],
        },
        "1.A.2.g.i-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.g.i-10546", "10308-10546"],
        },
        "1.A.2.g.i-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.g.i-10552", "10308-10552"],
        },
        "1.A.2.g.ii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.g.ii-10513", "10150-10513"],
        },
        "1.A.2.g.ii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.g.ii-10524", "10150-10524"],
        },
        "1.A.2.g.ii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.g.ii-10530", "10150-10530"],
        },
        "1.A.2.g.ii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.g.ii-10538", "10150-10538"],
        },
        "1.A.2.g.ii-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.g.ii-10546", "10150-10546"],
        },
        "1.A.2.g.ii-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.g.ii-10552", "10150-10552"],
        },
        "1.A.2.g.iii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.g.iii-10513", "8527-10513"],
        },
        "1.A.2.g.iii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.g.iii-10524", "8527-10524"],
        },
        "1.A.2.g.iii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.g.iii-10530", "8527-10530"],
        },
        "1.A.2.g.iii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.g.iii-10538", "8527-10538"],
        },
        "1.A.2.g.iii-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.g.iii-10546", "8527-10546"],
        },
        "1.A.2.g.iii-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.g.iii-10552", "8527-10552"],
        },
        "1.A.2.g.iv-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.g.iv-10513", "8424-10513"],
        },
        "1.A.2.g.iv-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.g.iv-10524", "8424-10524"],
        },
        "1.A.2.g.iv-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.g.iv-10530", "8424-10530"],
        },
        "1.A.2.g.iv-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.g.iv-10538", "8424-10538"],
        },
        "1.A.2.g.iv-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.g.iv-10546", "8424-10546"],
        },
        "1.A.2.g.iv-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.g.iv-10552", "8424-10552"],
        },
        "1.A.2.g.v-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.g.v-10513", "10287-10513"],
        },
        "1.A.2.g.v-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.g.v-10524", "10287-10524"],
        },
        "1.A.2.g.v-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.g.v-10530", "10287-10530"],
        },
        "1.A.2.g.v-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.g.v-10538", "10287-10538"],
        },
        "1.A.2.g.v-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.g.v-10546", "10287-10546"],
        },
        "1.A.2.g.v-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.g.v-10552", "10287-10552"],
        },
        "1.A.2.g.vi-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.g.vi-10513", "8721-10513"],
        },
        "1.A.2.g.vi-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.g.vi-10524", "8721-10524"],
        },
        "1.A.2.g.vi-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.g.vi-10530", "8721-10530"],
        },
        "1.A.2.g.vi-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.g.vi-10538", "8721-10538"],
        },
        "1.A.2.g.vi-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.g.vi-10546", "8721-10546"],
        },
        "1.A.2.g.vi-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.g.vi-10552", "8721-10552"],
        },
        "1.A.2.g.vii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.g.vii-10513", "8587-10513"],
        },
        "1.A.2.g.vii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.g.vii-10524", "8587-10524"],
        },
        "1.A.2.g.vii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.g.vii-10530", "8587-10530"],
        },
        "1.A.2.g.vii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.g.vii-10538", "8587-10538"],
        },
        "1.A.2.g.viii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.2.g.viii-10513", "8794-10513"],
        },
        "1.A.2.g.viii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.2.g.viii-10524", "8794-10524"],
        },
        "1.A.2.g.viii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.2.g.viii-10530", "8794-10530"],
        },
        "1.A.2.g.viii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.2.g.viii-10538", "8794-10538"],
        },
        "1.A.2.g.viii-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.2.g.viii-10546", "8794-10546"],
        },
        "1.A.2.g.viii-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.2.g.viii-10552", "8794-10552"],
        },
        "1.A.3-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3-10513", "8322-10513"],
        },
        "1.A.3-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3-10524", "8322-10524"],
        },
        "1.A.3-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3-10530", "8322-10530"],
        },
        "1.A.3-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3-10538", "8322-10538"],
        },
        "1.A.3-5": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.3-10552", "8322-10552"],
        },
        "1.A.3.a-1": {
            "title": "Aviation Gasoline",
            "alternative_codes": ["1.A.3.a-10512", "10419-10512"],
        },
        "1.A.3.a-2": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.a-10513", "10419-10513"],
        },
        "1.A.3.a-3": {
            "title": "Jet Kerosene",
            "alternative_codes": ["1.A.3.a-10526", "10419-10526"],
        },
        "1.A.3.a-4": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.a-10530", "10419-10530"],
        },
        "1.A.3.b-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.b-10513", "9607-10513"],
        },
        "1.A.3.b-2": {
            "title": "Diesel Oil",
            "alternative_codes": ["1.A.3.b-10520", "9607-10520"],
        },
        "1.A.3.b-3": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.b-10524", "9607-10524"],
        },
        "1.A.3.b-4": {
            "title": "Gasoline",
            "alternative_codes": ["1.A.3.b-10525", "9607-10525"],
        },
        "1.A.3.b-5": {
            "title": "Liquefied Petroleum Gases (LPG)",
            "alternative_codes": ["1.A.3.b-10528", "9607-10528"],
        },
        "1.A.3.b-6": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.b-10530", "9607-10530"],
        },
        "1.A.3.b-7": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.b-10538", "9607-10538"],
        },
        "1.A.3.b-8": {
            "title": "Other Liquid Fuels",
            "alternative_codes": ["1.A.3.b-10542", "9607-10542"],
        },
        "1.A.3.b.i-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.b.i-10513", "9279-10513"],
        },
        "1.A.3.b.i-2": {
            "title": "Diesel Oil",
            "alternative_codes": ["1.A.3.b.i-10520", "9279-10520"],
        },
        "1.A.3.b.i-3": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.b.i-10524", "9279-10524"],
        },
        "1.A.3.b.i-4": {
            "title": "Gasoline",
            "alternative_codes": ["1.A.3.b.i-10525", "9279-10525"],
        },
        "1.A.3.b.i-5": {
            "title": "Liquefied Petroleum Gases (LPG)",
            "alternative_codes": ["1.A.3.b.i-10528", "9279-10528"],
        },
        "1.A.3.b.i-6": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.b.i-10530", "9279-10530"],
        },
        "1.A.3.b.i-7": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.b.i-10538", "9279-10538"],
        },
        "1.A.3.b.i-8": {
            "title": "Other Liquid Fuels",
            "alternative_codes": ["1.A.3.b.i-10542", "9279-10542"],
        },
        "1.A.3.b.ii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.b.ii-10513", "9702-10513"],
        },
        "1.A.3.b.ii-2": {
            "title": "Diesel Oil",
            "alternative_codes": ["1.A.3.b.ii-10520", "9702-10520"],
        },
        "1.A.3.b.ii-3": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.b.ii-10524", "9702-10524"],
        },
        "1.A.3.b.ii-4": {
            "title": "Gasoline",
            "alternative_codes": ["1.A.3.b.ii-10525", "9702-10525"],
        },
        "1.A.3.b.ii-5": {
            "title": "Liquefied Petroleum Gases (LPG)",
            "alternative_codes": ["1.A.3.b.ii-10528", "9702-10528"],
        },
        "1.A.3.b.ii-6": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.b.ii-10530", "9702-10530"],
        },
        "1.A.3.b.ii-7": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.b.ii-10538", "9702-10538"],
        },
        "1.A.3.b.ii-8": {
            "title": "Other Liquid Fuels",
            "alternative_codes": ["1.A.3.b.ii-10542", "9702-10542"],
        },
        "1.A.3.b.iii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.b.iii-10513", "8358-10513"],
        },
        "1.A.3.b.iii-2": {
            "title": "Diesel Oil",
            "alternative_codes": ["1.A.3.b.iii-10520", "8358-10520"],
        },
        "1.A.3.b.iii-3": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.b.iii-10524", "8358-10524"],
        },
        "1.A.3.b.iii-4": {
            "title": "Gasoline",
            "alternative_codes": ["1.A.3.b.iii-10525", "8358-10525"],
        },
        "1.A.3.b.iii-5": {
            "title": "Liquefied Petroleum Gases (LPG)",
            "alternative_codes": ["1.A.3.b.iii-10528", "8358-10528"],
        },
        "1.A.3.b.iii-6": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.b.iii-10530", "8358-10530"],
        },
        "1.A.3.b.iii-7": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.b.iii-10538", "8358-10538"],
        },
        "1.A.3.b.iii-8": {
            "title": "Other Liquid Fuels",
            "alternative_codes": ["1.A.3.b.iii-10542", "8358-10542"],
        },
        "1.A.3.b.iv-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.b.iv-10513", "9622-10513"],
        },
        "1.A.3.b.iv-2": {
            "title": "Diesel Oil",
            "alternative_codes": ["1.A.3.b.iv-10520", "9622-10520"],
        },
        "1.A.3.b.iv-3": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.b.iv-10524", "9622-10524"],
        },
        "1.A.3.b.iv-4": {
            "title": "Gasoline",
            "alternative_codes": ["1.A.3.b.iv-10525", "9622-10525"],
        },
        "1.A.3.b.iv-5": {
            "title": "Liquefied Petroleum Gases (LPG)",
            "alternative_codes": ["1.A.3.b.iv-10528", "9622-10528"],
        },
        "1.A.3.b.iv-6": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.b.iv-10530", "9622-10530"],
        },
        "1.A.3.b.iv-7": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.b.iv-10538", "9622-10538"],
        },
        "1.A.3.b.iv-8": {
            "title": "Other Liquid Fuels",
            "alternative_codes": ["1.A.3.b.iv-10542", "9622-10542"],
        },
        "1.A.3.b.v-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.b.v-10513", "9083-10513"],
        },
        "1.A.3.b.v-2": {
            "title": "Diesel Oil",
            "alternative_codes": ["1.A.3.b.v-10520", "9083-10520"],
        },
        "1.A.3.b.v-3": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.b.v-10524", "9083-10524"],
        },
        "1.A.3.b.v-4": {
            "title": "Gasoline",
            "alternative_codes": ["1.A.3.b.v-10525", "9083-10525"],
        },
        "1.A.3.b.v-5": {
            "title": "Liquefied Petroleum Gases (LPG)",
            "alternative_codes": ["1.A.3.b.v-10528", "9083-10528"],
        },
        "1.A.3.b.v-6": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.b.v-10530", "9083-10530"],
        },
        "1.A.3.b.v-7": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.b.v-10538", "9083-10538"],
        },
        "1.A.3.b.v-8": {
            "title": "Other Liquid Fuels",
            "alternative_codes": ["1.A.3.b.v-10542", "9083-10542"],
        },
        "1.A.3.c-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.c-10513", "8924-10513"],
        },
        "1.A.3.c-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.c-10524", "8924-10524"],
        },
        "1.A.3.c-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.c-10530", "8924-10530"],
        },
        "1.A.3.c-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.c-10538", "8924-10538"],
        },
        "1.A.3.c-5": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.3.c-10552", "8924-10552"],
        },
        "1.A.3.d-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.d-10513", "9670-10513"],
        },
        "1.A.3.d-2": {
            "title": "Gas/Diesel Oil",
            "alternative_codes": ["1.A.3.d-10523", "9670-10523"],
        },
        "1.A.3.d-3": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.d-10524", "9670-10524"],
        },
        "1.A.3.d-4": {
            "title": "Gasoline",
            "alternative_codes": ["1.A.3.d-10525", "9670-10525"],
        },
        "1.A.3.d-5": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.d-10530", "9670-10530"],
        },
        "1.A.3.d-6": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.d-10538", "9670-10538"],
        },
        "1.A.3.d-7": {
            "title": "Other Liquid Fuels",
            "alternative_codes": ["1.A.3.d-10542", "9670-10542"],
        },
        "1.A.3.d-8": {
            "title": "Residual Fuel Oil",
            "alternative_codes": ["1.A.3.d-10549", "9670-10549"],
        },
        "1.A.3.e-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.e-10513", "8456-10513"],
        },
        "1.A.3.e-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.e-10524", "8456-10524"],
        },
        "1.A.3.e-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.e-10530", "8456-10530"],
        },
        "1.A.3.e-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.e-10538", "8456-10538"],
        },
        "1.A.3.e-5": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.3.e-10552", "8456-10552"],
        },
        "1.A.3.e.i-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.e.i-10513", "9504-10513"],
        },
        "1.A.3.e.i-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.e.i-10524", "9504-10524"],
        },
        "1.A.3.e.i-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.e.i-10530", "9504-10530"],
        },
        "1.A.3.e.i-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.e.i-10538", "9504-10538"],
        },
        "1.A.3.e.i-5": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.3.e.i-10552", "9504-10552"],
        },
        "1.A.3.e.ii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.3.e.ii-10513", "9935-10513"],
        },
        "1.A.3.e.ii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.3.e.ii-10524", "9935-10524"],
        },
        "1.A.3.e.ii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.3.e.ii-10530", "9935-10530"],
        },
        "1.A.3.e.ii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.3.e.ii-10538", "9935-10538"],
        },
        "1.A.3.e.ii-5": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.3.e.ii-10552", "9935-10552"],
        },
        "1.A.4-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4-10513", "9815-10513"],
        },
        "1.A.4-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4-10524", "9815-10524"],
        },
        "1.A.4-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4-10530", "9815-10530"],
        },
        "1.A.4-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4-10538", "9815-10538"],
        },
        "1.A.4-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.4-10546", "9815-10546"],
        },
        "1.A.4-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4-10552", "9815-10552"],
        },
        "1.A.4.a-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.a-10513", "8597-10513"],
        },
        "1.A.4.a-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.a-10524", "8597-10524"],
        },
        "1.A.4.a-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.a-10530", "8597-10530"],
        },
        "1.A.4.a-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.a-10538", "8597-10538"],
        },
        "1.A.4.a-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.4.a-10546", "8597-10546"],
        },
        "1.A.4.a-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4.a-10552", "8597-10552"],
        },
        "1.A.4.a.i-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.a.i-10513", "8216-10513"],
        },
        "1.A.4.a.i-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.a.i-10524", "8216-10524"],
        },
        "1.A.4.a.i-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.a.i-10530", "8216-10530"],
        },
        "1.A.4.a.i-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.a.i-10538", "8216-10538"],
        },
        "1.A.4.a.i-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.4.a.i-10546", "8216-10546"],
        },
        "1.A.4.a.i-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4.a.i-10552", "8216-10552"],
        },
        "1.A.4.a.ii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.a.ii-10513", "8251-10513"],
        },
        "1.A.4.a.ii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.a.ii-10524", "8251-10524"],
        },
        "1.A.4.a.ii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.a.ii-10530", "8251-10530"],
        },
        "1.A.4.a.ii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.a.ii-10538", "8251-10538"],
        },
        "1.A.4.a.ii-5": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4.a.ii-10552", "8251-10552"],
        },
        "1.A.4.a.iii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.a.iii-10513", "8223-10513"],
        },
        "1.A.4.a.iii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.a.iii-10524", "8223-10524"],
        },
        "1.A.4.a.iii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.a.iii-10530", "8223-10530"],
        },
        "1.A.4.a.iii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.a.iii-10538", "8223-10538"],
        },
        "1.A.4.a.iii-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.4.a.iii-10546", "8223-10546"],
        },
        "1.A.4.a.iii-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4.a.iii-10552", "8223-10552"],
        },
        "1.A.4.b-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.b-10513", "9823-10513"],
        },
        "1.A.4.b-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.b-10524", "9823-10524"],
        },
        "1.A.4.b-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.b-10530", "9823-10530"],
        },
        "1.A.4.b-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.b-10538", "9823-10538"],
        },
        "1.A.4.b-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.4.b-10546", "9823-10546"],
        },
        "1.A.4.b-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4.b-10552", "9823-10552"],
        },
        "1.A.4.b.i-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.b.i-10513", "8609-10513"],
        },
        "1.A.4.b.i-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.b.i-10524", "8609-10524"],
        },
        "1.A.4.b.i-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.b.i-10530", "8609-10530"],
        },
        "1.A.4.b.i-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.b.i-10538", "8609-10538"],
        },
        "1.A.4.b.i-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.4.b.i-10546", "8609-10546"],
        },
        "1.A.4.b.i-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4.b.i-10552", "8609-10552"],
        },
        "1.A.4.b.ii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.b.ii-10513", "10435-10513"],
        },
        "1.A.4.b.ii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.b.ii-10524", "10435-10524"],
        },
        "1.A.4.b.ii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.b.ii-10530", "10435-10530"],
        },
        "1.A.4.b.ii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.b.ii-10538", "10435-10538"],
        },
        "1.A.4.b.ii-5": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4.b.ii-10552", "10435-10552"],
        },
        "1.A.4.b.iii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.b.iii-10513", "8632-10513"],
        },
        "1.A.4.b.iii-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.b.iii-10524", "8632-10524"],
        },
        "1.A.4.b.iii-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.b.iii-10530", "8632-10530"],
        },
        "1.A.4.b.iii-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.b.iii-10538", "8632-10538"],
        },
        "1.A.4.b.iii-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.4.b.iii-10546", "8632-10546"],
        },
        "1.A.4.b.iii-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4.b.iii-10552", "8632-10552"],
        },
        "1.A.4.c-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.c-10513", "8554-10513"],
        },
        "1.A.4.c-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.c-10524", "8554-10524"],
        },
        "1.A.4.c-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.c-10530", "8554-10530"],
        },
        "1.A.4.c-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.c-10538", "8554-10538"],
        },
        "1.A.4.c-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.4.c-10546", "8554-10546"],
        },
        "1.A.4.c-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4.c-10552", "8554-10552"],
        },
        "1.A.4.c.i-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.c.i-10513", "8364-10513"],
        },
        "1.A.4.c.i-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.c.i-10524", "8364-10524"],
        },
        "1.A.4.c.i-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.c.i-10530", "8364-10530"],
        },
        "1.A.4.c.i-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.c.i-10538", "8364-10538"],
        },
        "1.A.4.c.i-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.4.c.i-10546", "8364-10546"],
        },
        "1.A.4.c.i-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.4.c.i-10552", "8364-10552"],
        },
        "1.A.4.c.ii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.c.ii-10513", "10080-10513"],
        },
        "1.A.4.c.ii-2": {
            "title": "Diesel Oil",
            "alternative_codes": ["1.A.4.c.ii-10520", "10080-10520"],
        },
        "1.A.4.c.ii-3": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.c.ii-10524", "10080-10524"],
        },
        "1.A.4.c.ii-4": {
            "title": "Gasoline",
            "alternative_codes": ["1.A.4.c.ii-10525", "10080-10525"],
        },
        "1.A.4.c.ii-5": {
            "title": "Liquefied Petroleum Gases (LPG)",
            "alternative_codes": ["1.A.4.c.ii-10528", "10080-10528"],
        },
        "1.A.4.c.ii-6": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.c.ii-10530", "10080-10530"],
        },
        "1.A.4.c.ii-7": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.c.ii-10538", "10080-10538"],
        },
        "1.A.4.c.ii-8": {
            "title": "Other Liquid Fuels",
            "alternative_codes": ["1.A.4.c.ii-10542", "10080-10542"],
        },
        "1.A.4.c.iii-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.4.c.iii-10513", "9812-10513"],
        },
        "1.A.4.c.iii-2": {
            "title": "Gas/Diesel Oil",
            "alternative_codes": ["1.A.4.c.iii-10523", "9812-10523"],
        },
        "1.A.4.c.iii-3": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.4.c.iii-10524", "9812-10524"],
        },
        "1.A.4.c.iii-4": {
            "title": "Gasoline",
            "alternative_codes": ["1.A.4.c.iii-10525", "9812-10525"],
        },
        "1.A.4.c.iii-5": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.4.c.iii-10530", "9812-10530"],
        },
        "1.A.4.c.iii-6": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.4.c.iii-10538", "9812-10538"],
        },
        "1.A.4.c.iii-7": {
            "title": "Other Liquid Fuels",
            "alternative_codes": ["1.A.4.c.iii-10542", "9812-10542"],
        },
        "1.A.4.c.iii-8": {
            "title": "Residual Fuel Oil",
            "alternative_codes": ["1.A.4.c.iii-10549", "9812-10549"],
        },
        "1.A.5-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.5-10513", "10273-10513"],
        },
        "1.A.5-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.5-10524", "10273-10524"],
        },
        "1.A.5-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.5-10530", "10273-10530"],
        },
        "1.A.5-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.5-10538", "10273-10538"],
        },
        "1.A.5-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.5-10546", "10273-10546"],
        },
        "1.A.5-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.5-10552", "10273-10552"],
        },
        "1.A.5.a-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.5.a-10513", "9861-10513"],
        },
        "1.A.5.a-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.5.a-10524", "9861-10524"],
        },
        "1.A.5.a-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.5.a-10530", "9861-10530"],
        },
        "1.A.5.a-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.5.a-10538", "9861-10538"],
        },
        "1.A.5.a-5": {
            "title": "Peat",
            "alternative_codes": ["1.A.5.a-10546", "9861-10546"],
        },
        "1.A.5.a-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.5.a-10552", "9861-10552"],
        },
        "1.A.5.b-1": {
            "title": "Biomass",
            "alternative_codes": ["1.A.5.b-10513", "9101-10513"],
        },
        "1.A.5.b-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.A.5.b-10524", "9101-10524"],
        },
        "1.A.5.b-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.A.5.b-10530", "9101-10530"],
        },
        "1.A.5.b-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.A.5.b-10538", "9101-10538"],
        },
        "1.A.5.b-5": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.A.5.b-10552", "9101-10552"],
        },
        "1.AA-1": {
            "title": "Biomass",
            "alternative_codes": ["1.AA-10513", "9089-10513"],
        },
        "1.AA-2": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.AA-10524", "9089-10524"],
        },
        "1.AA-3": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.AA-10530", "9089-10530"],
        },
        "1.AA-4": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.AA-10538", "9089-10538"],
        },
        "1.AA-5": {"title": "Peat", "alternative_codes": ["1.AA-10546", "9089-10546"]},
        "1.AA-6": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.AA-10552", "9089-10552"],
        },
        "1.AB-1": {
            "title": "Anthracite",
            "alternative_codes": ["1.AB-10511", "8533-10511"],
        },
        "1.AB-2": {
            "title": "Biomass",
            "alternative_codes": ["1.AB-10513", "8533-10513"],
        },
        "1.AB-3": {
            "title": "Bitumen",
            "alternative_codes": ["1.AB-10514", "8533-10514"],
        },
        "1.AB-4": {
            "title": "BKB and Patent Fuel",
            "alternative_codes": ["1.AB-10515", "8533-10515"],
        },
        "1.AB-5": {
            "title": "Coal Tar",
            "alternative_codes": ["1.AB-10516", "8533-10516"],
        },
        "1.AB-6": {
            "title": "Coke Oven/Gas Coke",
            "alternative_codes": ["1.AB-10517", "8533-10517"],
        },
        "1.AB-7": {
            "title": "Coking Coal",
            "alternative_codes": ["1.AB-10518", "8533-10518"],
        },
        "1.AB-8": {
            "title": "Crude Oil",
            "alternative_codes": ["1.AB-10519", "8533-10519"],
        },
        "1.AB-9": {
            "title": "Ethane",
            "alternative_codes": ["1.AB-10521", "8533-10521"],
        },
        "1.AB-10": {
            "title": "Gas Biomass",
            "alternative_codes": ["1.AB-10522", "8533-10522"],
        },
        "1.AB-11": {
            "title": "Gas/Diesel Oil",
            "alternative_codes": ["1.AB-10523", "8533-10523"],
        },
        "1.AB-12": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.AB-10524", "8533-10524"],
        },
        "1.AB-13": {
            "title": "Gasoline",
            "alternative_codes": ["1.AB-10525", "8533-10525"],
        },
        "1.AB-14": {
            "title": "Jet Kerosene",
            "alternative_codes": ["1.AB-10526", "8533-10526"],
        },
        "1.AB-15": {
            "title": "Lignite",
            "alternative_codes": ["1.AB-10527", "8533-10527"],
        },
        "1.AB-16": {
            "title": "Liquefied Petroleum Gases (LPG)",
            "alternative_codes": ["1.AB-10528", "8533-10528"],
        },
        "1.AB-17": {
            "title": "Liquid Biomass",
            "alternative_codes": ["1.AB-10529", "8533-10529"],
        },
        "1.AB-18": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.AB-10530", "8533-10530"],
        },
        "1.AB-19": {
            "title": "Lubricants",
            "alternative_codes": ["1.AB-10531", "8533-10531"],
        },
        "1.AB-20": {
            "title": "Naphtha",
            "alternative_codes": ["1.AB-10532", "8533-10532"],
        },
        "1.AB-21": {
            "title": "Natural Gas (Dry)",
            "alternative_codes": ["1.AB-10533", "8533-10533"],
        },
        "1.AB-22": {
            "title": "Natural Gas Liquids",
            "alternative_codes": ["1.AB-10534", "8533-10534"],
        },
        "1.AB-23": {
            "title": "Oil Shale and Tar Sand",
            "alternative_codes": ["1.AB-10535", "8533-10535"],
        },
        "1.AB-24": {
            "title": "Orimulsion",
            "alternative_codes": ["1.AB-10536", "8533-10536"],
        },
        "1.AB-25": {
            "title": "Other Bituminous Coal",
            "alternative_codes": ["1.AB-10537", "8533-10537"],
        },
        "1.AB-26": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.AB-10538", "8533-10538"],
        },
        "1.AB-27": {
            "title": "Other Gaseous Fossil",
            "alternative_codes": ["1.AB-10539", "8533-10539"],
        },
        "1.AB-28": {
            "title": "Other Kerosene",
            "alternative_codes": ["1.AB-10540", "8533-10540"],
        },
        "1.AB-29": {
            "title": "Other Liquid Fossil",
            "alternative_codes": ["1.AB-10541", "8533-10541"],
        },
        "1.AB-30": {
            "title": "Other non-fossil fuels (biogenic waste)",
            "alternative_codes": ["1.AB-10543", "8533-10543"],
        },
        "1.AB-31": {
            "title": "Other Oil",
            "alternative_codes": ["1.AB-10544", "8533-10544"],
        },
        "1.AB-32": {
            "title": "Other Solid Fossil",
            "alternative_codes": ["1.AB-10545", "8533-10545"],
        },
        "1.AB-33": {"title": "Peat", "alternative_codes": ["1.AB-10546", "8533-10546"]},
        "1.AB-34": {
            "title": "Petroleum Coke",
            "alternative_codes": ["1.AB-10547", "8533-10547"],
        },
        "1.AB-35": {
            "title": "Refinery Feedstocks",
            "alternative_codes": ["1.AB-10548", "8533-10548"],
        },
        "1.AB-36": {
            "title": "Residual Fuel Oil",
            "alternative_codes": ["1.AB-10549", "8533-10549"],
        },
        "1.AB-37": {
            "title": "Shale Oil",
            "alternative_codes": ["1.AB-10550", "8533-10550"],
        },
        "1.AB-38": {
            "title": "Solid Biomass",
            "alternative_codes": ["1.AB-10551", "8533-10551"],
        },
        "1.AB-39": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.AB-10552", "8533-10552"],
        },
        "1.AB-40": {
            "title": "Sub-bituminous Coal",
            "alternative_codes": ["1.AB-10553", "8533-10553"],
        },
        "1.AB-41": {
            "title": "Waste (non-biomass fraction)",
            "alternative_codes": ["1.AB-10554", "8533-10554"],
        },
        "1.AD-1": {
            "title": "Anthracite",
            "alternative_codes": ["1.AD-10511", "8731-10511"],
        },
        "1.AD-2": {
            "title": "Bitumen",
            "alternative_codes": ["1.AD-10514", "8731-10514"],
        },
        "1.AD-3": {
            "title": "BKB and Patent Fuel",
            "alternative_codes": ["1.AD-10515", "8731-10515"],
        },
        "1.AD-4": {
            "title": "Coal Tar",
            "alternative_codes": ["1.AD-10516", "8731-10516"],
        },
        "1.AD-5": {
            "title": "Coke Oven/Gas Coke",
            "alternative_codes": ["1.AD-10517", "8731-10517"],
        },
        "1.AD-6": {
            "title": "Coking Coal",
            "alternative_codes": ["1.AD-10518", "8731-10518"],
        },
        "1.AD-7": {
            "title": "Crude Oil",
            "alternative_codes": ["1.AD-10519", "8731-10519"],
        },
        "1.AD-8": {
            "title": "Ethane",
            "alternative_codes": ["1.AD-10521", "8731-10521"],
        },
        "1.AD-9": {
            "title": "Gas/Diesel Oil",
            "alternative_codes": ["1.AD-10523", "8731-10523"],
        },
        "1.AD-10": {
            "title": "Gaseous Fuels",
            "alternative_codes": ["1.AD-10524", "8731-10524"],
        },
        "1.AD-11": {
            "title": "Gasoline",
            "alternative_codes": ["1.AD-10525", "8731-10525"],
        },
        "1.AD-12": {
            "title": "Jet Kerosene",
            "alternative_codes": ["1.AD-10526", "8731-10526"],
        },
        "1.AD-13": {
            "title": "Lignite",
            "alternative_codes": ["1.AD-10527", "8731-10527"],
        },
        "1.AD-14": {
            "title": "Liquefied Petroleum Gases (LPG)",
            "alternative_codes": ["1.AD-10528", "8731-10528"],
        },
        "1.AD-15": {
            "title": "Liquid Fuels",
            "alternative_codes": ["1.AD-10530", "8731-10530"],
        },
        "1.AD-16": {
            "title": "Lubricants",
            "alternative_codes": ["1.AD-10531", "8731-10531"],
        },
        "1.AD-17": {
            "title": "Naphtha",
            "alternative_codes": ["1.AD-10532", "8731-10532"],
        },
        "1.AD-18": {
            "title": "Natural Gas (Dry)",
            "alternative_codes": ["1.AD-10533", "8731-10533"],
        },
        "1.AD-19": {
            "title": "Natural Gas Liquids",
            "alternative_codes": ["1.AD-10534", "8731-10534"],
        },
        "1.AD-20": {
            "title": "Oil Shale and Tar Sand",
            "alternative_codes": ["1.AD-10535", "8731-10535"],
        },
        "1.AD-21": {
            "title": "Orimulsion",
            "alternative_codes": ["1.AD-10536", "8731-10536"],
        },
        "1.AD-22": {
            "title": "Other Bituminous Coal",
            "alternative_codes": ["1.AD-10537", "8731-10537"],
        },
        "1.AD-23": {
            "title": "Other Fossil Fuels",
            "alternative_codes": ["1.AD-10538", "8731-10538"],
        },
        "1.AD-24": {
            "title": "Other Gaseous Fossil",
            "alternative_codes": ["1.AD-10539", "8731-10539"],
        },
        "1.AD-25": {
            "title": "Other Kerosene",
            "alternative_codes": ["1.AD-10540", "8731-10540"],
        },
        "1.AD-26": {
            "title": "Other Liquid Fossil",
            "alternative_codes": ["1.AD-10541", "8731-10541"],
        },
        "1.AD-27": {
            "title": "Other Oil",
            "alternative_codes": ["1.AD-10544", "8731-10544"],
        },
        "1.AD-28": {
            "title": "Other Solid Fossil",
            "alternative_codes": ["1.AD-10545", "8731-10545"],
        },
        "1.AD-29": {
            "title": "Petroleum Coke",
            "alternative_codes": ["1.AD-10547", "8731-10547"],
        },
        "1.AD-30": {
            "title": "Refinery Feedstocks",
            "alternative_codes": ["1.AD-10548", "8731-10548"],
        },
        "1.AD-31": {
            "title": "Residual Fuel Oil",
            "alternative_codes": ["1.AD-10549", "8731-10549"],
        },
        "1.AD-32": {
            "title": "Shale Oil",
            "alternative_codes": ["1.AD-10550", "8731-10550"],
        },
        "1.AD-33": {
            "title": "Solid Fuels",
            "alternative_codes": ["1.AD-10552", "8731-10552"],
        },
        "1.AD-34": {
            "title": "Sub-bituminous Coal",
            "alternative_codes": ["1.AD-10553", "8731-10553"],
        },
        "1.AD-35": {
            "title": "Waste (non-biomass fraction)",
            "alternative_codes": ["1.AD-10554", "8731-10554"],
        },
        "3.A-1": {"title": "Buffalo", "alternative_codes": ["3.A-10638", "9559-10638"]},
        "3.A-2": {"title": "Camels", "alternative_codes": ["3.A-10639", "9559-10639"]},
        "3.A-3": {"title": "Cattle", "alternative_codes": ["3.A-10640", "9559-10640"]},
        "3.A-4": {
            "title": "Dairy Cattle",
            "alternative_codes": ["3.A-10641", "9559-10641"],
        },
        "3.A-5": {"title": "Deer", "alternative_codes": ["3.A-10642", "9559-10642"]},
        "3.A-6": {
            "title": "Fur-bearing Animals",
            "alternative_codes": ["3.A-10643", "9559-10643"],
        },
        "3.A-7": {"title": "Goats", "alternative_codes": ["3.A-10644", "9559-10644"]},
        "3.A-8": {
            "title": "Growing Cattle",
            "alternative_codes": ["3.A-10645", "9559-10645"],
        },
        "3.A-9": {"title": "Horses", "alternative_codes": ["3.A-10646", "9559-10646"]},
        "3.A-10": {
            "title": "Mature Dairy Cattle",
            "alternative_codes": ["3.A-10647", "9559-10647"],
        },
        "3.A-11": {
            "title": "Mules and Asses",
            "alternative_codes": ["3.A-10648", "9559-10648"],
        },
        "3.A-12": {
            "title": "Non-Dairy Cattle",
            "alternative_codes": ["3.A-10649", "9559-10649"],
        },
        "3.A-13": {
            "title": "Ostrich",
            "alternative_codes": ["3.A-10650", "9559-10650"],
        },
        "3.A-14": {"title": "Other", "alternative_codes": ["3.A-10651", "9559-10651"]},
        "3.A-15": {
            "title": "Other Cattle",
            "alternative_codes": ["3.A-10652", "9559-10652"],
        },
        "3.A-16": {
            "title": "Other Mature Cattle",
            "alternative_codes": ["3.A-10653", "9559-10653"],
        },
        "3.A-17": {
            "title": "Poultry",
            "alternative_codes": ["3.A-10654", "9559-10654"],
        },
        "3.A-18": {"title": "Rabbit", "alternative_codes": ["3.A-10655", "9559-10655"]},
        "3.A-19": {
            "title": "Reindeer",
            "alternative_codes": ["3.A-10656", "9559-10656"],
        },
        "3.A-20": {"title": "Sheep", "alternative_codes": ["3.A-10657", "9559-10657"]},
        "3.A-21": {"title": "Swine", "alternative_codes": ["3.A-10658", "9559-10658"]},
        "3.B-1": {"title": "Buffalo", "alternative_codes": ["3.B-10638", "9608-10638"]},
        "3.B-2": {"title": "Camels", "alternative_codes": ["3.B-10639", "9608-10639"]},
        "3.B-3": {"title": "Cattle", "alternative_codes": ["3.B-10640", "9608-10640"]},
        "3.B-4": {
            "title": "Dairy Cattle",
            "alternative_codes": ["3.B-10641", "9608-10641"],
        },
        "3.B-5": {"title": "Deer", "alternative_codes": ["3.B-10642", "9608-10642"]},
        "3.B-6": {
            "title": "Fur-bearing Animals",
            "alternative_codes": ["3.B-10643", "9608-10643"],
        },
        "3.B-7": {"title": "Goats", "alternative_codes": ["3.B-10644", "9608-10644"]},
        "3.B-8": {
            "title": "Growing Cattle",
            "alternative_codes": ["3.B-10645", "9608-10645"],
        },
        "3.B-9": {"title": "Horses", "alternative_codes": ["3.B-10646", "9608-10646"]},
        "3.B-10": {
            "title": "Mature Dairy Cattle",
            "alternative_codes": ["3.B-10647", "9608-10647"],
        },
        "3.B-11": {
            "title": "Mules and Asses",
            "alternative_codes": ["3.B-10648", "9608-10648"],
        },
        "3.B-12": {
            "title": "Non-Dairy Cattle",
            "alternative_codes": ["3.B-10649", "9608-10649"],
        },
        "3.B-13": {
            "title": "Ostrich",
            "alternative_codes": ["3.B-10650", "9608-10650"],
        },
        "3.B-14": {"title": "Other", "alternative_codes": ["3.B-10651", "9608-10651"]},
        "3.B-15": {
            "title": "Other Cattle",
            "alternative_codes": ["3.B-10652", "9608-10652"],
        },
        "3.B-16": {
            "title": "Other Mature Cattle",
            "alternative_codes": ["3.B-10653", "9608-10653"],
        },
        "3.B-17": {
            "title": "Poultry",
            "alternative_codes": ["3.B-10654", "9608-10654"],
        },
        "3.B-18": {"title": "Rabbit", "alternative_codes": ["3.B-10655", "9608-10655"]},
        "3.B-19": {
            "title": "Reindeer",
            "alternative_codes": ["3.B-10656", "9608-10656"],
        },
        "3.B-20": {"title": "Sheep", "alternative_codes": ["3.B-10657", "9608-10657"]},
        "3.B-21": {"title": "Swine", "alternative_codes": ["3.B-10658", "9608-10658"]},
        "4-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4-10820", "9411-10820"],
        },
        "4-2": {
            "title": "4 (IV) Indirect N2O emissions from managed soils - Atmospheric Deposition",
            "alternative_codes": ["4-10821", "9411-10821"],
        },
        "4-3": {
            "title": "4 (IV) Indirect N2O emissions from managed soils - Nitrogen Leaching and Run-off",
            "alternative_codes": ["4-10822", "9411-10822"],
        },
        "4-4": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4-10824", "9411-10824"],
        },
        "4-5": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4-10825", "9411-10825"],
        },
        "4-6": {
            "title": "4 (II) Emissions and removals from drainage and rewetting and other management of organic and mineral soils",
            "alternative_codes": ["4-10826", "9411-10826"],
        },
        "4.A-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.A-10820", "10121-10820"],
        },
        "4.A-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.A-10824", "10121-10824"],
        },
        "4.A-3": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4.A-10825", "10121-10825"],
        },
        "4.A-4": {
            "title": "4 (II) Emissions and removals from drainage and rewetting and other management of organic and mineral soils",
            "alternative_codes": ["4.A-10826", "10121-10826"],
        },
        "4.A-5": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.A-10827", "10121-10827"],
        },
        "4.A-6": {
            "title": "Drained Organic Soils",
            "alternative_codes": ["4.A-10829", "10121-10829"],
        },
        "4.A-7": {
            "title": "Other Mineral Soils",
            "alternative_codes": ["4.A-10832", "10121-10832"],
        },
        "4.A-8": {
            "title": "Other Organic Soils",
            "alternative_codes": ["4.A-10833", "10121-10833"],
        },
        "4.A-9": {
            "title": "Rewetted Mineral Soils",
            "alternative_codes": ["4.A-10834", "10121-10834"],
        },
        "4.A-10": {
            "title": "Rewetted Organic Soils",
            "alternative_codes": ["4.A-10835", "10121-10835"],
        },
        "4.A-11": {
            "title": "Total mineral soils",
            "alternative_codes": ["4.A-10836", "10121-10836"],
        },
        "4.A-12": {
            "title": "Total organic soils",
            "alternative_codes": ["4.A-10837", "10121-10837"],
        },
        "4.A.1-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.A.1-10820", "8348-10820"],
        },
        "4.A.1-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.A.1-10824", "8348-10824"],
        },
        "4.A.1-3": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4.A.1-10825", "8348-10825"],
        },
        "4.A.1-4": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.A.1-10827", "8348-10827"],
        },
        "4.A.1-5": {
            "title": "Controlled Burning",
            "alternative_codes": ["4.A.1-10828", "8348-10828"],
        },
        "4.A.1-6": {
            "title": "Inorganic N Fertilizers",
            "alternative_codes": ["4.A.1-10830", "8348-10830"],
        },
        "4.A.1-7": {
            "title": "Organic N Fertilizers",
            "alternative_codes": ["4.A.1-10831", "8348-10831"],
        },
        "4.A.1-8": {
            "title": "Wildfires",
            "alternative_codes": ["4.A.1-10838", "8348-10838"],
        },
        "4.A.2-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.A.2-10820", "8416-10820"],
        },
        "4.A.2-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.A.2-10824", "8416-10824"],
        },
        "4.A.2-3": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4.A.2-10825", "8416-10825"],
        },
        "4.A.2-4": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.A.2-10827", "8416-10827"],
        },
        "4.A.2-5": {
            "title": "Controlled Burning",
            "alternative_codes": ["4.A.2-10828", "8416-10828"],
        },
        "4.A.2-6": {
            "title": "Inorganic N Fertilizers",
            "alternative_codes": ["4.A.2-10830", "8416-10830"],
        },
        "4.A.2-7": {
            "title": "Organic N Fertilizers",
            "alternative_codes": ["4.A.2-10831", "8416-10831"],
        },
        "4.A.2-8": {
            "title": "Wildfires",
            "alternative_codes": ["4.A.2-10838", "8416-10838"],
        },
        "4.A.2.a-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.A.2.a-10820", "9741-10820"],
        },
        "4.A.2.a-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.A.2.a-10827", "9741-10827"],
        },
        "4.A.2.b-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.A.2.b-10820", "9851-10820"],
        },
        "4.A.2.b-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.A.2.b-10827", "9851-10827"],
        },
        "4.A.2.c-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.A.2.c-10820", "9306-10820"],
        },
        "4.A.2.c-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.A.2.c-10827", "9306-10827"],
        },
        "4.A.2.d-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.A.2.d-10820", "10297-10820"],
        },
        "4.A.2.d-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.A.2.d-10827", "10297-10827"],
        },
        "4.A.2.e-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.A.2.e-10820", "8735-10820"],
        },
        "4.A.2.e-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.A.2.e-10827", "8735-10827"],
        },
        "4.B-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.B-10820", "9805-10820"],
        },
        "4.B-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.B-10824", "9805-10824"],
        },
        "4.B-3": {
            "title": "4 (II) Emissions and removals from drainage and rewetting and other management of organic and mineral soils",
            "alternative_codes": ["4.B-10826", "9805-10826"],
        },
        "4.B-4": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.B-10827", "9805-10827"],
        },
        "4.B-5": {
            "title": "Drained Organic Soils",
            "alternative_codes": ["4.B-10829", "9805-10829"],
        },
        "4.B-6": {
            "title": "Other Mineral Soils",
            "alternative_codes": ["4.B-10832", "9805-10832"],
        },
        "4.B-7": {
            "title": "Other Organic Soils",
            "alternative_codes": ["4.B-10833", "9805-10833"],
        },
        "4.B-8": {
            "title": "Rewetted Mineral Soils",
            "alternative_codes": ["4.B-10834", "9805-10834"],
        },
        "4.B-9": {
            "title": "Rewetted Organic Soils",
            "alternative_codes": ["4.B-10835", "9805-10835"],
        },
        "4.B-10": {
            "title": "Total mineral soils",
            "alternative_codes": ["4.B-10836", "9805-10836"],
        },
        "4.B-11": {
            "title": "Total organic soils",
            "alternative_codes": ["4.B-10837", "9805-10837"],
        },
        "4.B.1-1": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.B.1-10824", "10430-10824"],
        },
        "4.B.1-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.B.1-10827", "10430-10827"],
        },
        "4.B.1-3": {
            "title": "Controlled Burning",
            "alternative_codes": ["4.B.1-10828", "10430-10828"],
        },
        "4.B.1-4": {
            "title": "Wildfires",
            "alternative_codes": ["4.B.1-10838", "10430-10838"],
        },
        "4.B.2-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.B.2-10820", "8678-10820"],
        },
        "4.B.2-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.B.2-10824", "8678-10824"],
        },
        "4.B.2-3": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.B.2-10827", "8678-10827"],
        },
        "4.B.2-4": {
            "title": "Controlled Burning",
            "alternative_codes": ["4.B.2-10828", "8678-10828"],
        },
        "4.B.2-5": {
            "title": "Wildfires",
            "alternative_codes": ["4.B.2-10838", "8678-10838"],
        },
        "4.B.2.a-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.B.2.a-10820", "9799-10820"],
        },
        "4.B.2.a-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.B.2.a-10827", "9799-10827"],
        },
        "4.B.2.b-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.B.2.b-10820", "9491-10820"],
        },
        "4.B.2.b-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.B.2.b-10827", "9491-10827"],
        },
        "4.B.2.c-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.B.2.c-10820", "10450-10820"],
        },
        "4.B.2.c-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.B.2.c-10827", "10450-10827"],
        },
        "4.B.2.d-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.B.2.d-10820", "8709-10820"],
        },
        "4.B.2.d-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.B.2.d-10827", "8709-10827"],
        },
        "4.B.2.e-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.B.2.e-10820", "9560-10820"],
        },
        "4.B.2.e-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.B.2.e-10827", "9560-10827"],
        },
        "4.C-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.C-10820", "8849-10820"],
        },
        "4.C-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.C-10824", "8849-10824"],
        },
        "4.C-3": {
            "title": "4 (II) Emissions and removals from drainage and rewetting and other management of organic and mineral soils",
            "alternative_codes": ["4.C-10826", "8849-10826"],
        },
        "4.C-4": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.C-10827", "8849-10827"],
        },
        "4.C-5": {
            "title": "Drained Organic Soils",
            "alternative_codes": ["4.C-10829", "8849-10829"],
        },
        "4.C-6": {
            "title": "Other Mineral Soils",
            "alternative_codes": ["4.C-10832", "8849-10832"],
        },
        "4.C-7": {
            "title": "Other Organic Soils",
            "alternative_codes": ["4.C-10833", "8849-10833"],
        },
        "4.C-8": {
            "title": "Rewetted Mineral Soils",
            "alternative_codes": ["4.C-10834", "8849-10834"],
        },
        "4.C-9": {
            "title": "Rewetted Organic Soils",
            "alternative_codes": ["4.C-10835", "8849-10835"],
        },
        "4.C-10": {
            "title": "Total mineral soils",
            "alternative_codes": ["4.C-10836", "8849-10836"],
        },
        "4.C-11": {
            "title": "Total organic soils",
            "alternative_codes": ["4.C-10837", "8849-10837"],
        },
        "4.C.1-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.C.1-10820", "9360-10820"],
        },
        "4.C.1-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.C.1-10824", "9360-10824"],
        },
        "4.C.1-3": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.C.1-10827", "9360-10827"],
        },
        "4.C.1-4": {
            "title": "Controlled Burning",
            "alternative_codes": ["4.C.1-10828", "9360-10828"],
        },
        "4.C.1-5": {
            "title": "Wildfires",
            "alternative_codes": ["4.C.1-10838", "9360-10838"],
        },
        "4.C.2-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.C.2-10820", "8259-10820"],
        },
        "4.C.2-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.C.2-10824", "8259-10824"],
        },
        "4.C.2-3": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.C.2-10827", "8259-10827"],
        },
        "4.C.2-4": {
            "title": "Controlled Burning",
            "alternative_codes": ["4.C.2-10828", "8259-10828"],
        },
        "4.C.2-5": {
            "title": "Wildfires",
            "alternative_codes": ["4.C.2-10838", "8259-10838"],
        },
        "4.C.2.a-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.C.2.a-10820", "9405-10820"],
        },
        "4.C.2.a-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.C.2.a-10827", "9405-10827"],
        },
        "4.C.2.b-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.C.2.b-10820", "9966-10820"],
        },
        "4.C.2.b-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.C.2.b-10827", "9966-10827"],
        },
        "4.C.2.c-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.C.2.c-10820", "10323-10820"],
        },
        "4.C.2.c-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.C.2.c-10827", "10323-10827"],
        },
        "4.C.2.d-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.C.2.d-10820", "9444-10820"],
        },
        "4.C.2.d-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.C.2.d-10827", "9444-10827"],
        },
        "4.C.2.e-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.C.2.e-10820", "10189-10820"],
        },
        "4.C.2.e-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.C.2.e-10827", "10189-10827"],
        },
        "4.D-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.D-10820", "9897-10820"],
        },
        "4.D-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.D-10824", "9897-10824"],
        },
        "4.D-3": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4.D-10825", "9897-10825"],
        },
        "4.D-4": {
            "title": "4 (II) Emissions and removals from drainage and rewetting and other management of organic and mineral soils",
            "alternative_codes": ["4.D-10826", "9897-10826"],
        },
        "4.D-5": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D-10827", "9897-10827"],
        },
        "4.D.1-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.D.1-10820", "9154-10820"],
        },
        "4.D.1-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.D.1-10824", "9154-10824"],
        },
        "4.D.1-3": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4.D.1-10825", "9154-10825"],
        },
        "4.D.1-4": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.1-10827", "9154-10827"],
        },
        "4.D.1-5": {
            "title": "Controlled Burning",
            "alternative_codes": ["4.D.1-10828", "9154-10828"],
        },
        "4.D.1-6": {
            "title": "Inorganic N Fertilizers",
            "alternative_codes": ["4.D.1-10830", "9154-10830"],
        },
        "4.D.1-7": {
            "title": "Organic N Fertilizers",
            "alternative_codes": ["4.D.1-10831", "9154-10831"],
        },
        "4.D.1-8": {
            "title": "Wildfires",
            "alternative_codes": ["4.D.1-10838", "9154-10838"],
        },
        "4.D.1.a-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.1.a-10827", "10156-10827"],
        },
        "4.D.1.b-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.1.b-10827", "9151-10827"],
        },
        "4.D.1.c-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.1.c-10827", "8307-10827"],
        },
        "4.D.2-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.D.2-10820", "8232-10820"],
        },
        "4.D.2-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.D.2-10824", "8232-10824"],
        },
        "4.D.2-3": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4.D.2-10825", "8232-10825"],
        },
        "4.D.2-4": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2-10827", "8232-10827"],
        },
        "4.D.2-5": {
            "title": "Controlled Burning",
            "alternative_codes": ["4.D.2-10828", "8232-10828"],
        },
        "4.D.2-6": {
            "title": "Inorganic N Fertilizers",
            "alternative_codes": ["4.D.2-10830", "8232-10830"],
        },
        "4.D.2-7": {
            "title": "Organic N Fertilizers",
            "alternative_codes": ["4.D.2-10831", "8232-10831"],
        },
        "4.D.2-8": {
            "title": "Wildfires",
            "alternative_codes": ["4.D.2-10838", "8232-10838"],
        },
        "4.D.2.a-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.a-10827", "11002-10827"],
        },
        "4.D.2.b-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.b-10827", "11003-10827"],
        },
        "4.D.2.b.i-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.b.i-10827", "11004-10827"],
        },
        "4.D.2.b.ii-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.b.ii-10827", "11005-10827"],
        },
        "4.D.2.b.iii-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.b.iii-10827", "11006-10827"],
        },
        "4.D.2.b.iv-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.b.iv-10827", "11007-10827"],
        },
        "4.D.2.b.v-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.b.v-10827", "11008-10827"],
        },
        "4.D.2.c-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.c-10827", "11009-10827"],
        },
        "4.D.2.c.i-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.D.2.c.i-10820", "11010-10820"],
        },
        "4.D.2.c.i-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.c.i-10827", "11010-10827"],
        },
        "4.D.2.c.ii-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.D.2.c.ii-10820", "11011-10820"],
        },
        "4.D.2.c.ii-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.c.ii-10827", "11011-10827"],
        },
        "4.D.2.c.iii-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.D.2.c.iii-10820", "11012-10820"],
        },
        "4.D.2.c.iii-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.c.iii-10827", "11012-10827"],
        },
        "4.D.2.c.iv-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.D.2.c.iv-10820", "11013-10820"],
        },
        "4.D.2.c.iv-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.c.iv-10827", "11013-10827"],
        },
        "4.D.2.c.v-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.D.2.c.v-10820", "11014-10820"],
        },
        "4.D.2.c.v-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.D.2.c.v-10827", "11014-10827"],
        },
        "4.E-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.E-10820", "10314-10820"],
        },
        "4.E-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.E-10824", "10314-10824"],
        },
        "4.E-3": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4.E-10825", "10314-10825"],
        },
        "4.E-4": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.E-10827", "10314-10827"],
        },
        "4.E.1-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.E.1-10820", "10132-10820"],
        },
        "4.E.1-2": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4.E.1-10825", "10132-10825"],
        },
        "4.E.1-3": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.E.1-10827", "10132-10827"],
        },
        "4.E.1-4": {
            "title": "Inorganic N Fertilizers",
            "alternative_codes": ["4.E.1-10830", "10132-10830"],
        },
        "4.E.1-5": {
            "title": "Organic N Fertilizers",
            "alternative_codes": ["4.E.1-10831", "10132-10831"],
        },
        "4.E.2-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.E.2-10820", "9506-10820"],
        },
        "4.E.2-2": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4.E.2-10825", "9506-10825"],
        },
        "4.E.2-3": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.E.2-10827", "9506-10827"],
        },
        "4.E.2-4": {
            "title": "Inorganic N Fertilizers",
            "alternative_codes": ["4.E.2-10830", "9506-10830"],
        },
        "4.E.2-5": {
            "title": "Organic N Fertilizers",
            "alternative_codes": ["4.E.2-10831", "9506-10831"],
        },
        "4.E.2.a-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.E.2.a-10820", "10183-10820"],
        },
        "4.E.2.a-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.E.2.a-10827", "10183-10827"],
        },
        "4.E.2.b-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.E.2.b-10820", "9914-10820"],
        },
        "4.E.2.b-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.E.2.b-10827", "9914-10827"],
        },
        "4.E.2.c-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.E.2.c-10820", "10026-10820"],
        },
        "4.E.2.c-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.E.2.c-10827", "10026-10827"],
        },
        "4.E.2.d-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.E.2.d-10820", "8465-10820"],
        },
        "4.E.2.d-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.E.2.d-10827", "8465-10827"],
        },
        "4.E.2.e-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.E.2.e-10820", "9857-10820"],
        },
        "4.E.2.e-2": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.E.2.e-10827", "9857-10827"],
        },
        "4.F-1": {
            "title": "4 (III) Direct N2O Emissions from N Mineralization/ Immobilization",
            "alternative_codes": ["4.F-10820", "8288-10820"],
        },
        "4.F-2": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.F-10824", "8288-10824"],
        },
        "4.F-3": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.F-10827", "8288-10827"],
        },
        "4.F.1-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.F.1-10827", "11015-10827"],
        },
        "4.F.2-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.F.2-10827", "8343-10827"],
        },
        "4.F.2.a-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.F.2.a-10827", "8488-10827"],
        },
        "4.F.2.b-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.F.2.b-10827", "8234-10827"],
        },
        "4.F.2.c-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.F.2.c-10827", "8574-10827"],
        },
        "4.F.2.d-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.F.2.d-10827", "10371-10827"],
        },
        "4.F.2.e-1": {
            "title": "Carbon stock change",
            "alternative_codes": ["4.F.2.e-10827", "9019-10827"],
        },
        "4.H-1": {
            "title": "4 (V) Biomass Burning",
            "alternative_codes": ["4.H-10824", "9158-10824"],
        },
        "4.H-2": {
            "title": "4 (I) Direct N2O Emissions from N inputs to managed soils",
            "alternative_codes": ["4.H-10825", "9158-10825"],
        },
        "4.H-3": {
            "title": "4 (II) Emissions and removals from drainage and rewetting and other management of organic and mineral soils",
            "alternative_codes": ["4.H-10826", "9158-10826"],
        },
        "2.F.1.a-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.F.1.a-m10809", "9129-m10809"],
        },
        "2.F.1.a-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.1.a-m10810", "9129-m10810"],
        },
        "2.F.1.a-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.1.a-m10811", "9129-m10811"],
        },
        "2.F.1.b-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.F.1.b-m10809", "9780-m10809"],
        },
        "2.F.1.b-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.1.b-m10810", "9780-m10810"],
        },
        "2.F.1.b-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.1.b-m10811", "9780-m10811"],
        },
        "2.F.1.c-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.F.1.c-m10809", "10252-m10809"],
        },
        "2.F.1.c-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.1.c-m10810", "10252-m10810"],
        },
        "2.F.1.c-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.1.c-m10811", "10252-m10811"],
        },
        "2.F.1.d-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.F.1.d-m10809", "9634-m10809"],
        },
        "2.F.1.d-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.1.d-m10810", "9634-m10810"],
        },
        "2.F.1.d-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.1.d-m10811", "9634-m10811"],
        },
        "2.F.1.e-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.F.1.e-m10809", "10244-m10809"],
        },
        "2.F.1.e-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.1.e-m10810", "10244-m10810"],
        },
        "2.F.1.e-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.1.e-m10811", "10244-m10811"],
        },
        "2.F.1.f-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.F.1.f-m10809", "10298-m10809"],
        },
        "2.F.1.f-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.1.f-m10810", "10298-m10810"],
        },
        "2.F.1.f-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.1.f-m10811", "10298-m10811"],
        },
        "2.F.2.a-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.F.2.a-m10809", "8642-m10809"],
        },
        "2.F.2.a-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.2.a-m10810", "8642-m10810"],
        },
        "2.F.2.a-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.2.a-m10811", "8642-m10811"],
        },
        "2.F.2.b-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.2.b-m10810", "9224-m10810"],
        },
        "2.F.2.b-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.2.b-m10811", "9224-m10811"],
        },
        "2.F.3-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.F.3-m10809", "9296-m10809"],
        },
        "2.F.3-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.3-m10810", "9296-m10810"],
        },
        "2.F.3-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.3-m10811", "9296-m10811"],
        },
        "2.F.4.a-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.4.a-m10810", "8519-m10810"],
        },
        "2.F.4.a-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.4.a-m10811", "8519-m10811"],
        },
        "2.F.5-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.F.5-m10809", "8316-m10809"],
        },
        "2.F.5-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.5-m10810", "8316-m10810"],
        },
        "2.F.5-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.5-m10811", "8316-m10811"],
        },
        "2.F.6.a-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.6.a-m10810", "10246-m10810"],
        },
        "2.F.6.a-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.6.a-m10811", "10246-m10811"],
        },
        "2.F.6.b-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.F.6.b-m10809", "10042-m10809"],
        },
        "2.F.6.b-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.F.6.b-m10810", "10042-m10810"],
        },
        "2.F.6.b-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.F.6.b-m10811", "10042-m10811"],
        },
        "2.G.1-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.G.1-m10809", "9490-m10809"],
        },
        "2.G.1-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.G.1-m10810", "9490-m10810"],
        },
        "2.G.1-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.G.1-m10811", "9490-m10811"],
        },
        "2.G.2.a-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.G.2.a-m10809", "9055-m10809"],
        },
        "2.G.2.a-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.G.2.a-m10810", "9055-m10810"],
        },
        "2.G.2.a-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.G.2.a-m10811", "9055-m10811"],
        },
        "2.G.2.b-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.G.2.b-m10809", "9925-m10809"],
        },
        "2.G.2.b-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.G.2.b-m10810", "9925-m10810"],
        },
        "2.G.2.b-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.G.2.b-m10811", "9925-m10811"],
        },
        "2.G.2.c-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.G.2.c-m10809", "9789-m10809"],
        },
        "2.G.2.c-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.G.2.c-m10810", "9789-m10810"],
        },
        "2.G.2.c-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.G.2.c-m10811", "9789-m10811"],
        },
        "2.G.2.d-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.G.2.d-m10809", "9610-m10809"],
        },
        "2.G.2.d-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.G.2.d-m10810", "9610-m10810"],
        },
        "2.G.2.d-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.G.2.d-m10811", "9610-m10811"],
        },
        "2.H.1-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.H.1-m10809", "8644-m10809"],
        },
        "2.H.1-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.H.1-m10810", "8644-m10810"],
        },
        "2.H.1-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.H.1-m10811", "8644-m10811"],
        },
        "2.H.2-m3": {
            "title": "Emissions from disposal",
            "alternative_codes": ["2.H.2-m10809", "8797-m10809"],
        },
        "2.H.2-m1": {
            "title": "Emissions from manufacturing",
            "alternative_codes": ["2.H.2-m10810", "8797-m10810"],
        },
        "2.H.2-m2": {
            "title": "Emissions from stocks",
            "alternative_codes": ["2.H.2-m10811", "8797-m10811"],
        },
    },
}
