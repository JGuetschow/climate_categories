spec = {
    "name": "CRF1999",
    "title": "Common Reporting Format GHG emissions categories (1999)",
    "comment": "Classification of green-house gas emissions and removals into categories for use in annual inventories using the Common Reporting Format as specified in the UNFCCC guidelines on reporting and review as decided in the fifth session of the Conference of the Parties in 1999",
    "references": "United Nations 2000, Review of the Implementation of Commitments and of Other Provisions of the Convention, Annex Common Reporting Format, UNDOC FCCC/CP/1999/7, pages 15ff, https://undocs.org/en/FCCC/CP/1999/7",
    "institution": "UN",
    "hierarchical": True,
    "last_update": "1999-11-05",
    "version": "1999",
    "total_sum": True,
    "canonical_top_level_category": "0",
    "categories": {
        "0": {
            "title": "Total National Emissions and Removals",
            "children": [["1", "2", "3", "4", "5", "6", "7"]],
        },
        "1": {
            "title": "Energy",
            "comment": "Total emission of all greenhouse gases from stationary and mobile energy activities (fuel combustion as well as fugitive fuel emissions). Sum of categories I A & B.",
            "children": [["1.A", "1.B"]],
        },
        "1.A": {
            "title": "Fuel Combustion Activities",
            "comment": "Total emissions of all greenhouse gases from all fuel combustion activities as described further below. CO2 emissions from combustion of biomass fuels are not included in totals for the energy sector. They may not be net emissions if the biomass is sustainably produced. If biomass is harvested at an unsustainable rate (that is, faster than annual regrowth), net CO2 emissions will appear as a loss of biomass stocks in the Land-Use Change and Forestry module. Other greenhouse gases from biomass fuel combustion are considered net emissions and are reported under Energy. (Sum of I A 1 to I A 5). Incineration of waste for waste-to-energy facilities should be reported here and not under Section 6C. Emissions based upon fuel for use on ships or aircraft engaged in international transport (1 A 3 a i and 1 A 3 d i) should, as far as possible, not be included in national totals but reported separately.",
            "alternative_codes": ["1A", "1 A"],
            "children": [["1.A.1", "1.A.2", "1.A.3", "1.A.4", "1.A.5"], ["1.A-ref"]],
        },
        "1.A.1": {
            "title": "Energy Industries",
            "comment": "Comprises emissions from fuels combusted by the fuel extraction or energy producing industries.",
            "alternative_codes": ["1A1", "1 A 1"],
            "children": [["1.A.1.a", "1.A.1.b", "1.A.1.c"]],
        },
        "1.A.1.a": {
            "title": "Public Electricity and Heat Production",
            "comment": "Sum of emissions from public electricity generation, public combined heat and power generation, and public heat plants. Public utilities are defined as those undertakings whose primary activity is to supply the public. They may be in public or private ownership. Emissions from own on-site use of fuel should be included. Emissions from autoproducers (undertakings which generate electricity/heat wholly or partly for their own use, as an activity which supports their primary activity) should be assigned to the sector where they were generated and not under 1 A 1 a. Autoproducers may be in public or private ownership.",
            "alternative_codes": ["1A1a", "1 A 1 a"],
            "children": [["1.A.1.a.i", "1.A.1.a.ii", "1.A.1.a.iii"]],
        },
        "1.A.1.a.i": {
            "title": "Public Electricity Generation",
            "comment": "Comprises emissions from all fuel use for electricity generation except those from combined heat and power plants.",
            "alternative_codes": ["1A1ai", "1 A 1 a i"],
        },
        "1.A.1.a.ii": {
            "title": "Public Combined Heat and Power Generation (Chp)",
            "comment": "Emissions from production of both heat and electrical power for sale to the public, at a single facility; co-generation plant.",
            "alternative_codes": ["1A1aii", "1 A 1 a ii"],
        },
        "1.A.1.a.iii": {
            "title": "Public Heat Plants",
            "comment": "Production of heat for sale by pipe network.",
            "alternative_codes": ["1A1aiii", "1 A 1 a iii"],
        },
        "1.A.1.b": {
            "title": "Petroleum Refining",
            "comment": "All combustion activities supporting the refining of petroleum products. Does not include evaporative emissions, which should be reported separately under 1 A 3 b v or 1 B 2 a below.",
            "alternative_codes": ["1A1b", "1 A 1 b"],
        },
        "1.A.1.c": {
            "title": "Manufacture of Solid Fuels and Other Energy Industries",
            "comment": "Combustion emissions from fuel use during the manufacture of secondary and tertiary products from solid fuels including production of charcoal. Emissions from own on-site fuel use should be included.",
            "alternative_codes": ["1A1c", "1 A 1 c"],
            "children": [["1.A.1.c.i", "1.A.1.c.ii"]],
        },
        "1.A.1.c.i": {
            "title": "Manufacture of Solid Fuels",
            "comment": "Emissions arising from fuel combustion for the production of coke, brown coal briquettes and patent fuel.",
            "alternative_codes": ["1A1ci", "1 A 1 c i"],
        },
        "1.A.1.c.ii": {
            "title": "Other Energy Industries",
            "comment": "Combustion emissions arising from the energy-producing industries own (onsite) energy use not mentioned above. This includes the emissions from own-energy use in coal mining and oil and gas extraction. Combustion emissions from pipeline transport should be reported under 1 A 3 e.",
            "alternative_codes": ["1A1cii", "1 A 1 c ii"],
        },
        "1.A.2": {
            "title": "Manufacturing Industries and Construction",
            "comment": "Emissions from combustion of fuels in industry including combustion for the generation of electricity and heat. Emissions from autoproducers should be assigned to the sector where they were generated and an attempt made to separately identify the emissions associated with autogeneration from those associated with process heat. Emissions from fuel combustion in coke ovens within the iron and steel industry should be reported under 1 A 1 c and not within manufacturing industry. Emissions from the industry sector should be specified by subsectors that correspond to the International Standard Industrial Classification of All Economic Activities, 3rd Edition (ISIC)  [International Standard Industrial Classification of all Economic Activities, Series M No. 4, Rev. 3, United Nations, New York, 1990]. Energy used for transport by industry should not be reported here but under Transport (1 A 3 below). Emissions arising from off-road and other mobile machinery in industry should, if possible, be broken out as a separate subcategory. For each country, the emissions from the largest fuel-consuming industrial categories (ISIC) should be reported, as well as those from significant emitters of pollutants. A suggested list of categories is outlined below.",
            "alternative_codes": ["1A2", "1 A 2"],
            "children": [
                ["1.A.2.a", "1.A.2.b", "1.A.2.c", "1.A.2.d", "1.A.2.e", "1.A.2.f"]
            ],
        },
        "1.A.2.a": {
            "title": "Iron and Steel",
            "comment": "ISIC Group 271 and Class 2731",
            "alternative_codes": ["1A2a", "1 A 2 a"],
        },
        "1.A.2.b": {
            "title": "Non-Ferrous Metals",
            "comment": "ISIC Group 272 and Class 2732",
            "alternative_codes": ["1A2b", "1 A 2 b"],
        },
        "1.A.2.c": {
            "title": "Chemicals",
            "comment": "ISIC Division 24",
            "alternative_codes": ["1A2c", "1 A 2 c"],
        },
        "1.A.2.d": {
            "title": "Pulp, Paper and Print",
            "comment": "ISIC Divisions 21 and 22",
            "alternative_codes": ["1A2d", "1 A 2 d"],
        },
        "1.A.2.e": {
            "title": "Food Processing, Beverages and Tobacco",
            "comment": "ISIC Divisions 15 and 16",
            "alternative_codes": ["1A2e", "1 A 2 e"],
        },
        "1.A.2.f": {
            "title": "Other",
            "comment": "The remaining emissions from fuel combustion in industry should be reported here. This also includes emissions from the construction branch. Please specify what is reported, as far as possible by ISIC categories. Care should be taken not to double count emissions from construction by including them also in Categories 1 A 3 e ii and/or 1 A 5.",
            "alternative_codes": ["1A2f", "1 A 2 f"],
        },
        "1.A.3": {
            "title": "Transport",
            "comment": "Emissions from the combustion and evaporation of fuel for all transport activity, regardless of the sector, specified by subsectors as follows. Emissions from fuel sold to any air or marine vessel engaged in international transport (international bunker fuels) should as far as possible be excluded from the totals and subtotals in this category and should be reported separately.",
            "alternative_codes": ["1A3", "1 A 3"],
            "children": [["1.A.3.a", "1.A.3.b", "1.A.3.c", "1.A.3.d", "1.A.3.e"]],
        },
        "1.A.3.a": {
            "title": "Civil Aviation",
            "comment": "Emissions from international civil aviation and domestic air transport (commercial, private, agricultural, etc.), including take-offs and landings. Exclude use of fuel at airports for ground transport which is reported under 1 A 3 e Other Transportation (below). Also exclude fuel for stationary combustion at airports; report this information under the appropriate stationary combustion category.",
            "alternative_codes": ["1A3a", "1 A 3 a"],
            "children": [["1.A.3.a.i", "1.A.3.a.ii"]],
        },
        "1.A.3.a.i": {
            "title": "International Aviation (International Bunkers)",
            "comment": "Emissions which relate to fuel use for international civil aviation. Note that these emissions are to be excluded as far as possible from national totals but should be reported separately. (In other inventory methodologies, landing and take-off (LTO) cycle emissions are often considered as domestic emissions. For the purpose of greenhouse gas emissions inventories, fuel used during landing and take-off for an international flight stage is considered to be part of International Bunkers fuel use.)",
            "alternative_codes": ["1A3ai", "1 A 3 a i"],
        },
        "1.A.3.a.ii": {
            "title": "Domestic",
            "comment": "Includes all civil domestic passenger and freight traffic inside a country (not used as international bunkers) and including take-offs and landings for these flight stages.",
            "alternative_codes": ["1A3aii", "1 A 3 a ii"],
        },
        "1.A.3.b": {
            "title": "Road Transportation",
            "comment": "All combustion and evaporative emissions arising from fuel use in road vehicles, including the use of agricultural vehicles on highways.",
            "alternative_codes": ["1A3b", "1 A 3 b"],
            "children": [
                ["1.A.3.b.i", "1.A.3.b.ii", "1.A.3.b.iii", "1.A.3.b.iv", "1.A.3.b.v"]
            ],
        },
        "1.A.3.b.i": {
            "title": "Cars",
            "comment": "Automobiles designated primarily for transport of persons and having a capacity of 12 persons or fewer. Gross vehicle weight rating of 3900 kg or less.",
            "alternative_codes": ["1A3bi", "1 A 3 b i"],
            "children": [["1.A.3.b.i.1", "1.A.3.b.i.2"]],
        },
        "1.A.3.b.i.1": {
            "title": "Passenger Cars with 3-Way Catalysts",
            "comment": "Passenger car emissions from vehicles with 3-way catalysts.",
            "alternative_codes": ["1A3bi1", "1 A 3 b i 1"],
        },
        "1.A.3.b.i.2": {
            "title": "Passenger Cars without 3-Way Catalysts",
            "comment": "Passenger car emissions from vehicles without 3-way catalysts.",
            "alternative_codes": ["1A3bi2", "1 A 3 b i 2"],
        },
        "1.A.3.b.ii": {
            "title": "Light Duty Trucks",
            "comment": "Vehicles with a gross vehicle weight of 3900 kg or less designated primarily for transportation of light-weight cargo or which are equipped with special features such as four-wheel drive for off-road operation.",
            "alternative_codes": ["1A3bii", "1 A 3 b ii"],
            "children": [["1.A.3.b.ii.1", "1.A.3.b.ii.2"]],
        },
        "1.A.3.b.ii.1": {
            "title": "Light Duty Trucks with 3- Way Catalysts",
            "comment": "Light Duty Truck emissions from vehicles with 3-way catalysts.",
            "alternative_codes": ["1A3bii1", "1 A 3 b ii 1"],
        },
        "1.A.3.b.ii.2": {
            "title": "Light Duty Trucks without 3-Way Catalysts",
            "comment": "Light Duty Truck emissions from vehicles without 3-way catalysts.",
            "alternative_codes": ["1A3bii2", "1 A 3 b ii 2"],
        },
        "1.A.3.b.iii": {
            "title": "Heavy Duty Trucks and Buses",
            "comment": "Any vehicle rated at more than 3900 kg gross vehicle weight or designed to carry more than 12 persons at a time.",
            "alternative_codes": ["1A3biii", "1 A 3 b iii"],
        },
        "1.A.3.b.iv": {
            "title": "Motorcycles",
            "comment": "Any motor vehicle designed to travel with not more than three wheels in contact with the ground and weighing less than 680 kg.",
            "alternative_codes": ["1A3biv", "1 A 3 b iv"],
        },
        "1.A.3.b.v": {
            "title": "Evaporative Emissions from Vehicles",
            "comment": "Evaporative emissions are included here (they are estimated with the same activity data as are used for estimating combustion emissions).",
            "alternative_codes": ["1A3bv", "1 A 3 b v"],
        },
        "1.A.3.c": {
            "title": "Railways",
            "comment": "Includes emissions from both freight and passenger traffic routes.",
            "alternative_codes": ["1A3c", "1 A 3 c"],
        },
        "1.A.3.d": {
            "title": "Navigation",
            "comment": "Emissions from fuels used to propel water-borne vessels, including hovercraft and hydrofoils.",
            "alternative_codes": ["1A3d", "1 A 3 d"],
            "children": [["1.A.3.d.i", "1.A.3.d.ii"]],
        },
        "1.A.3.d.i": {
            "title": "International Marine (Bunkers)",
            "comment": "Comprises emissions from fuels burned by sea-going ships of all flags that are engaged in international transport. These emissions should as far as possible be excluded from national totals and reported separately.",
            "alternative_codes": ["1A3di", "1 A 3 d i"],
        },
        "1.A.3.d.ii": {
            "title": "National Navigation",
            "comment": "Emissions from fuel used for navigation of all vessels not engaged in international transport, except fishing (which should be reported under 1 A 4 c iii). Note that this may include journeys of considerable length between two ports in a country (e.g. San Francisco to Honolulu).",
            "alternative_codes": ["1A3dii", "1 A 3 d ii"],
        },
        "1.A.3.e": {
            "title": "Other Transportation",
            "comment": "Combustion emissions from all remaining transport activities including pipeline transportation, ground activities in airports and harbours, and off-road activities not otherwise reported under 1 A 4 c Agriculture or 1 A 2. Manufacturing Industries and Construction. Military transport should be reported under 1 A 5 (see I A 5 Other, below).",
            "alternative_codes": ["1A3e", "1 A 3 e"],
            "children": [["1.A.3.e.i", "1.A.3.e.ii"]],
        },
        "1.A.3.e.i": {
            "title": "Pipeline Transport",
            "alternative_codes": ["1A3ei", "1 A 3 e i"],
        },
        "1.A.3.e.ii": {
            "title": "Off -Road",
            "alternative_codes": ["1A3eii", "1 A 3 e ii"],
        },
        "1.A.4": {
            "title": "Other Sectors",
            "comment": "Emission from combustion activities as described below. Emissions from autoproducers should be assigned to the sector where they were generated and an attempt made to separately identify the emissions associated with autogeneration from those associated with process heat.",
            "alternative_codes": ["1A4", "1 A 4"],
            "children": [["1.A.4.a", "1.A.4.b", "1.A.4.c"]],
        },
        "1.A.4.a": {
            "title": "Commercial / Institutional",
            "comment": "Emission from fuel combustion in commercial and institutional buildings. (All activities included in ISIC categories 4103, 42, 6, 719, 72, 8, and 91-96).",
            "alternative_codes": ["1A4a", "1 A 4 a"],
        },
        "1.A.4.b": {
            "title": "Residential",
            "comment": "All emissions from fuel combustion in households.",
            "alternative_codes": ["1A4b", "1 A 4 b"],
        },
        "1.A.4.c": {
            "title": "Agriculture / Forestry / Fishing",
            "comment": "Emissions from fuel combustion in agriculture, forestry, or domestic inland, coastal and deep-sea fishing. This includes traction vehicles, pump fuel use, grain drying, horticultural greenhouses and other agriculture, forestry or fishing related fuel use. (Activities included in ISIC categories 05, 11, 12, 1302). Highway agricultural transportation is excluded.",
            "alternative_codes": ["1A4c", "1 A 4 c"],
            "children": [["1.A.4.c.i", "1.A.4.c.ii", "1.A.4.c.iii"]],
        },
        "1.A.4.c.i": {
            "title": "Stationary",
            "alternative_codes": ["1A4ci", "1 A 4 c i"],
        },
        "1.A.4.c.ii": {
            "title": "Off-Road Vehicles and Other Machinery",
            "alternative_codes": ["1A4cii", "1 A 4 c ii"],
        },
        "1.A.4.c.iii": {
            "title": "Fishing",
            "alternative_codes": ["1A4ciii", "1 A 4 c iii"],
        },
        "1.A.5": {
            "title": "Other",
            "comment": "All remaining emissions from non-specified fuel combustion. Include emissions from military fuel use.",
            "alternative_codes": ["1A5", "1 A 5"],
            "children": [["1.A.5.a", "1.A.5.b"]],
        },
        "1.A.5.a": {"title": "Stationary", "alternative_codes": ["1A5a", "1 A 5 a"]},
        "1.A.5.b": {
            "title": "Mobile",
            "comment": "Vehicles and Other Machinery, Marine and Aviation (not included in 1 A 4 c ii or elsewhere).",
            "alternative_codes": ["1A5b", "1 A 5 b"],
        },
        "1.B": {
            "title": "Fugitive Emissions from Fuels",
            "comment": "Fugitive emissions are intentional or unintentional releases of gases from anthropogenic activities. In particular, they may arise from the production, processing, transmission, storage and use of fuels, and include emissions from combustion only where it does not support a productive activity (e.g., flaring of natural gases at oil and gas production facilities). Evaporative emissions from vehicles are included under Road Transport as Subsection 1 A 3 b v. Sum of 1 B 1 & 1 B 2.",
            "alternative_codes": ["1B", "1 B"],
            "children": [["1.B.1", "1.B.2"]],
        },
        "1.B.1": {
            "title": "Solid Fuels",
            "comment": "Total release of methane during coal mining and post-mining activities. Combustion emissions from colliery methane recovered and used should be excluded here and reported under Fuel Combustion Emissions.",
            "alternative_codes": ["1B1", "1 B 1"],
            "children": [["1.B.1.a", "1.B.1.b", "1.B.1.c"]],
        },
        "1.B.1.a": {
            "title": "Coal Mining",
            "comment": "Total emissions from underground and surface mining and post-mining activities.",
            "alternative_codes": ["1B1a", "1 B 1 a"],
            "children": [["1.B.1.a.i", "1.B.1.a.ii"]],
        },
        "1.B.1.a.i": {
            "title": "Underground Mines",
            "alternative_codes": ["1B1ai", "1 B 1 a i"],
            "children": [["1.B.1.a.i.1", "1.B.1.a.i.2"]],
        },
        "1.B.1.a.i.1": {
            "title": "Mining Activities",
            "comment": "Emissions from underground mines, brought to the surface by ventilation systems.",
            "alternative_codes": ["1B1ai1", "1 B 1 a i 1"],
        },
        "1.B.1.a.i.2": {
            "title": "Post-Mining Activities",
            "comment": "Emissions from coal after extraction from the ground, which occur during preparation, transportation, storage, or final crushing prior to combustion.",
            "alternative_codes": ["1B1ai2", "1 B 1 a i 2"],
        },
        "1.B.1.a.ii": {
            "title": "Surface Mines",
            "comment": "Total emissions from surface mining and post-mining activities.",
            "alternative_codes": ["1B1aii", "1 B 1 a ii"],
            "children": [["1.B.1.a.ii.1", "1.B.1.a.ii.2"]],
        },
        "1.B.1.a.ii.1": {
            "title": "Mining Activities",
            "comment": "Emissions primarily from the exposed coal surfaces and coal rubble, but also emissions associated with the release of pressure on the coal.",
            "alternative_codes": ["1B1aii1", "1 B 1 a ii 1"],
        },
        "1.B.1.a.ii.2": {
            "title": "Post-Mining Ativities",
            "comment": "Emissions from coal after extraction from the ground, during preparation, transportation, storage, or final crushing prior to combustion.",
            "alternative_codes": ["1B1aii2", "1 B 1 a ii 2"],
        },
        "1.B.1.b": {
            "title": "Solid Fuel Transformation",
            "comment": "Fugitive emissions arising during the manufacture of secondary and tertiary products from solid fuels.",
            "alternative_codes": ["1B1b", "1 B 1 b"],
        },
        "1.B.1.c": {
            "title": "Other",
            "comment": "Fugitive emissions from fuel treatment plants not elsewhere specified.",
            "alternative_codes": ["1B1c", "1 B 1 c"],
        },
        "1.B.2": {
            "title": "Oil and Natural Gas",
            "comment": "Total fugitive emissions from oil and gas activities. Fugitive emissions may arise from equipment exhaust (non-combustion), leakages, upsets and mishaps at any point in the chain from production through final use. Note also that emissions from flaring are included (the combustion is considered a nonproductive activity).",
            "alternative_codes": ["1B2", "1 B 2"],
            "children": [["1.B.2.a", "1.B.2.b", "1.B.2.c", "1.B.2.d"]],
        },
        "1.B.2.a": {
            "title": "Oil",
            "alternative_codes": ["1B2a", "1 B 2 a"],
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
            "comment": "Fugitive emissions from oil exploration only.",
            "alternative_codes": ["1B2ai", "1 B 2 a i"],
        },
        "1.B.2.a.ii": {
            "title": "Production",
            "comment": "Fugitive emissions from the production of crude oil only.",
            "alternative_codes": ["1B2aii", "1 B 2 a ii"],
        },
        "1.B.2.a.iii": {
            "title": "Transport",
            "comment": "Fugitive emissions resulting from the loading and unloading of crude oil from tankers.",
            "alternative_codes": ["1B2aiii", "1 B 2 a iii"],
        },
        "1.B.2.a.iv": {
            "title": "Refining/ Storage",
            "comment": "Fugitive emissions from the refining of oil and from storage in tanks.",
            "alternative_codes": ["1B2aiv", "1 B 2 a iv"],
        },
        "1.B.2.a.v": {
            "title": "Distribution of Oil Products",
            "comment": "Emissions (primarily NMVOCs) from transport and handling of oil products.",
            "alternative_codes": ["1B2av", "1 B 2 a v"],
        },
        "1.B.2.a.vi": {"title": "Other", "alternative_codes": ["1B2avi", "1 B 2 a vi"]},
        "1.B.2.b": {
            "title": "Natural Gas",
            "alternative_codes": ["1B2b", "1 B 2 b"],
            "children": [
                ["1.B.2.b-dis", "1.B.2.b-exp", "1.B.2.b.i", "1.B.2.b.ii", "1.B.2.b.iii"]
            ],
        },
        "1.B.2.b.i": {
            "title": "Production/ Processing",
            "comment": "Emissions from the production of gas, gas gathering systems and gas separation plants.",
            "alternative_codes": ["1B2bi", "1 B 2 b i"],
        },
        "1.B.2.b.ii": {
            "title": "Transmission/ Distribution",
            "comment": "Emissions from pipelines for long distance and local transport of methane, compressor stations and their maintenance facilities.",
            "alternative_codes": ["1B2bii", "1 B 2 b ii"],
        },
        "1.B.2.b.iii": {
            "title": "Other Leakage",
            "comment": "Release of gas at point of use, including residential, commercial, industrial and electricity generation users.",
            "alternative_codes": ["1B2biii", "1 B 2 b iii"],
            "children": [["1.B.2.b.iii.1", "1.B.2.b.iii.2"]],
        },
        "1.B.2.c": {
            "title": "Venting and Flaring",
            "comment": "The release and/or combustion of excess gas at facilities for the production of oil or gas and for the processing of gas.",
            "alternative_codes": ["1B2c", "1 B 2 c"],
            "children": [["1.B.2.c-fla", "1.B.2.c-ven"]],
        },
        "2": {
            "title": "Industrial Processes",
            "comment": "Emissions within this sector comprise by-product or fugitive emissions of greenhouse gases from industrial processes. Emissions from fuel combustion in industry should be reported under Energy. In instances where industrial process emissions result jointly from chemical processes and fuel combustion it may be difficult to assign the emission(s) to either sector. Where the main purpose of the fuel combustion is to use the heat released, the resulting emissions should be assigned to the Energy sector. Emissions should, wherever possible, be reported according to the ISIC Group or Class within which they occur. Certain methods in Chapter and Module 2, however, infer final GHG emissions from supply of the GHG, equipment containing it (for example, air conditioning equipment) or a stock material with which emissions are linked (for example, limestone). In these cases, assignment of emissions to ISIC activities may be difficult or incomplete.",
            "children": [["2.A", "2.B", "2.C", "2.D", "2.E", "2.F", "2.G"]],
        },
        "2.A": {
            "title": "Mineral Products",
            "comment": "ISIC2 Division 26",
            "alternative_codes": ["2A", "2 A"],
            "children": [
                ["2.A.1", "2.A.2", "2.A.3", "2.A.4", "2.A.5", "2.A.6", "2.A.7"]
            ],
        },
        "2.A.1": {"title": "Cement Production", "alternative_codes": ["2A1", "2 A 1"]},
        "2.A.2": {"title": "Lime Production", "alternative_codes": ["2A2", "2 A 2"]},
        "2.A.3": {
            "title": "Limestone and Dolomite Use",
            "alternative_codes": ["2A3", "2 A 3"],
        },
        "2.A.4": {
            "title": "Soda Ash Production and Use",
            "alternative_codes": ["2A4", "2 A 4"],
        },
        "2.A.5": {"title": "Asphalt Roofing", "alternative_codes": ["2A5", "2 A 5"]},
        "2.A.6": {
            "title": "Road Paving with Asphalt",
            "alternative_codes": ["2A6", "2 A 6"],
        },
        "2.A.7": {
            "title": "Other",
            "comment": "Please specify.",
            "alternative_codes": ["2A7", "2 A 7"],
            "children": [["2.A.7.a", "2.A.7.b"]],
        },
        "2.B": {
            "title": "Chemical Industry",
            "comment": "ISIC Division 24",
            "alternative_codes": ["2B", "2 B"],
            "children": [["2.B.1", "2.B.2", "2.B.3", "2.B.4", "2.B.5"]],
        },
        "2.B.1": {"title": "Ammonia Production", "alternative_codes": ["2B1", "2 B 1"]},
        "2.B.2": {
            "title": "Nitric Acid Production",
            "alternative_codes": ["2B2", "2 B 2"],
        },
        "2.B.3": {
            "title": "Adipic Acid Production",
            "alternative_codes": ["2B3", "2 B 3"],
        },
        "2.B.4": {
            "title": "Carbide Production",
            "alternative_codes": ["2B4", "2 B 4"],
            "children": [["2.B.4.a", "2.B.4.b"]],
        },
        "2.B.5": {
            "title": "Other",
            "comment": "Please specify.",
            "alternative_codes": ["2B5", "2 B 5"],
            "children": [
                ["2.B.5.a", "2.B.5.b", "2.B.5.c", "2.B.5.d", "2.B.5.e", "2.B.5.f"]
            ],
        },
        "2.C": {
            "title": "Metal Production",
            "comment": "ISIC Division 27",
            "alternative_codes": ["2C", "2 C"],
            "children": [["2.C.1", "2.C.2", "2.C.3", "2.C.4", "2.C.5"]],
        },
        "2.C.1": {
            "title": "Iron and Steel Production",
            "alternative_codes": ["2C1", "2 C 1"],
            "children": [["2.C.1.a", "2.C.1.b", "2.C.1.c", "2.C.1.d", "2.C.1.e"]],
        },
        "2.C.2": {
            "title": "Ferroalloys Production",
            "alternative_codes": ["2C2", "2 C 2"],
        },
        "2.C.3": {
            "title": "Aluminium Production",
            "alternative_codes": ["2C3", "2 C 3"],
        },
        "2.C.4": {
            "title": "SF6 used in Aluminium and Magnesium Foundries",
            "alternative_codes": ["2C4", "2 C 4"],
            "children": [["2.C.4.a", "2.C.4.b"]],
        },
        "2.C.5": {
            "title": "Other",
            "comment": "Please specify.",
            "alternative_codes": ["2C5", "2 C 5"],
        },
        "2.D": {
            "title": "Other Production",
            "comment": "ISIC Divisions 15 and 29",
            "alternative_codes": ["2D", "2 D"],
            "children": [["2.D.1", "2.D.2"]],
        },
        "2.D.1": {"title": "Pulp and Paper", "alternative_codes": ["2D1", "2 D 1"]},
        "2.D.2": {"title": "Food and Drink", "alternative_codes": ["2D2", "2 D 2"]},
        "2.E": {
            "title": "Production of Halocarbons and Sulphur Hexafluoride",
            "comment": "Possibly ISIC Class 2411 or 2429",
            "alternative_codes": ["2E", "2 E"],
            "children": [["2.E.1", "2.E.2", "2.E.3"]],
        },
        "2.E.1": {
            "title": "By-Product Emissions",
            "alternative_codes": ["2E1", "2 E 1"],
            "children": [["2.E.1.a", "2.E.1.b"]],
        },
        "2.E.2": {"title": "Fugitive Emissions", "alternative_codes": ["2E2", "2 E 2"]},
        "2.E.3": {
            "title": "Other",
            "comment": "Please specify.",
            "alternative_codes": ["2E3", "2 E 3"],
        },
        "2.F": {
            "title": "Consumption of Halocarbons and Sulphur Hexafluoride",
            "alternative_codes": ["2F", "2 F"],
            "children": [
                ["2.F.1", "2.F.2", "2.F.3", "2.F.4", "2.F.5", "2.F.6", "2.F.7", "2.F.8"]
            ],
        },
        "2.F.1": {
            "title": "Refrigeration and Air Conditioning Equipment",
            "alternative_codes": ["2F1", "2 F 1"],
            "children": [
                ["2.F.1.a", "2.F.1.b", "2.F.1.c", "2.F.1.d", "2.F.1.e", "2.F.1.f"]
            ],
        },
        "2.F.2": {
            "title": "Foam Blowing",
            "alternative_codes": ["2F2", "2 F 2"],
            "children": [["2.F.2.a", "2.F.2.b"]],
        },
        "2.F.3": {"title": "Fire Extinguishers", "alternative_codes": ["2F3", "2 F 3"]},
        "2.F.4": {
            "title": "Aerosols / Metered Dose Inhalers",
            "alternative_codes": ["2F4", "2 F 4"],
            "children": [["2.F.4.a", "2.F.4.b"]],
        },
        "2.F.5": {"title": "Solvents", "alternative_codes": ["2F5", "2 F 5"]},
        "2.G": {"title": "Other", "alternative_codes": ["2G", "2 G"]},
        "3": {
            "title": "Solvent and Other Product Use",
            "comment": "This category covers mainly NMVOC emissions resulting from the use of solvents and other products containing volatile compounds. When the solvents and other products are, or are produced from, petroleum products, the carbon in the NMVOC emissions will be included in the CO2 inventory if the Reference Approach for CO2 emissions from energy is used. See note on double counting in “Overview of the IPCC Guidelines”. Emissions from the consumption of halocarbons and sulphur hexafluoride should be reported in the Industrial Processes Chapter under 2 F. All other non-energy emissions not included under Industrial Processes are reported here.",
            "children": [["3.A", "3.B", "3.C", "3.D"]],
        },
        "3.A": {"title": "Paint Application", "alternative_codes": ["3A", "3 A"]},
        "3.B": {
            "title": "Degreasing & Dry Cleaning",
            "alternative_codes": ["3B", "3 B"],
        },
        "3.C": {
            "title": "Chemical Products, Manufacture & Processing",
            "alternative_codes": ["3C", "3 C"],
        },
        "3.D": {
            "title": "Other",
            "comment": "Includes use of N2O as a carrier gas, anaesthetic, and propellant.",
            "alternative_codes": ["3D", "3 D"],
            "children": [["3.D.1", "3.D.2", "3.D.3", "3.D.4", "3.D.5"]],
        },
        "4": {
            "title": "Agriculture",
            "comment": "Describes all anthropogenic emissions from this sector except for fuel combustion and sewage emissions, which are covered in Energy 1 A and Waste 6 B, respectively. Sum of all agriculture categories 4 A, B, C, D, E, F & G.",
            "children": [["4.A", "4.B", "4.C", "4.D", "4.E", "4.F", "4.G"]],
        },
        "4.A": {
            "title": "Enteric Fermentation",
            "comment": "Methane production from herbivores as a by-product of enteric fermentation, a digestive process by which carbohydrates are broken down by micro-organisms into simple molecules for absorption into the bloodstream. Both ruminant (e.g. cattle, sheep) and non-ruminant animals (e.g. pigs, horses) produce CH4, although ruminants are the largest source (per unit of feed intake).",
            "alternative_codes": ["4A", "4 A"],
            "children": [
                [
                    "4.A.1",
                    "4.A.10",
                    "4.A.2",
                    "4.A.3",
                    "4.A.4",
                    "4.A.5",
                    "4.A.6",
                    "4.A.7",
                    "4.A.8",
                    "4.A.9",
                ]
            ],
        },
        "4.A.1": {
            "title": "Cattle",
            "alternative_codes": ["4A1", "4 A 1"],
            "children": [["4.A.1.a", "4.A.1.b"]],
        },
        "4.A.1.a": {
            "title": "Dairy",
            "comment": "Cattle producing milk for commercial exchange and calves and heifers being grown for dairy purposes.",
            "alternative_codes": ["4A1a", "4 A 1 a"],
        },
        "4.A.1.b": {
            "title": "Non-Dairy",
            "comment": "All non-dairy cattle including: cattle kept or grown for meat production, draft animals, and breeding animals.",
            "alternative_codes": ["4A1b", "4 A 1 b"],
        },
        "4.A.2": {"title": "Buffalo", "alternative_codes": ["4A2", "4 A 2"]},
        "4.A.3": {"title": "Sheep", "alternative_codes": ["4A3", "4 A 3"]},
        "4.A.4": {"title": "Goats", "alternative_codes": ["4A4", "4 A 4"]},
        "4.A.5": {"title": "Camels and Llamas", "alternative_codes": ["4A5", "4 A 5"]},
        "4.A.6": {"title": "Horses", "alternative_codes": ["4A6", "4 A 6"]},
        "4.A.7": {"title": "Mules and Asses", "alternative_codes": ["4A7", "4 A 7"]},
        "4.A.8": {"title": "Swine", "alternative_codes": ["4A8", "4 A 8"]},
        "4.A.9": {"title": "Poultry", "alternative_codes": ["4A9", "4 A 9"]},
        "4.A.10": {
            "title": "Other",
            "comment": "Please specify.",
            "alternative_codes": ["4A10", "4 A 10"],
        },
        "4.B": {
            "title": "Manure Management",
            "comment": "Methane and nitrous oxide are produced from the decomposition of manure under low oxygen or anaerobic conditions. These conditions often occur when large numbers of animals are managed in a confined area (e.g. dairy farms, beef feedlots, and swine and poultry farms), where manure is typically stored in large piles or disposed of in lagoons and other types of manure management systems. Methane emissions are covered in Sections 4 B 1 to 4 B 9 and N2O emissions in Sections 4 B 10 to 4 B 12 below.",
            "alternative_codes": ["4B", "4 B"],
            "children": [
                [
                    "4.B.1",
                    "4.B.10",
                    "4.B.11",
                    "4.B.12",
                    "4.B.13",
                    "4.B.2",
                    "4.B.3",
                    "4.B.4",
                    "4.B.5",
                    "4.B.6",
                    "4.B.7",
                    "4.B.8",
                    "4.B.9",
                ]
            ],
        },
        "4.B.1": {
            "title": "Cattle",
            "alternative_codes": ["4B1", "4 B 1"],
            "children": [["4.B.1.a", "4.B.1.b"]],
        },
        "4.B.1.a": {"title": "Dairy", "alternative_codes": ["4B1a", "4 B 1 a"]},
        "4.B.1.b": {"title": "Non-Dairy", "alternative_codes": ["4B1b", "4 B 1 b"]},
        "4.B.2": {"title": "Buffalo", "alternative_codes": ["4B2", "4 B 2"]},
        "4.B.3": {"title": "Sheep", "alternative_codes": ["4B3", "4 B 3"]},
        "4.B.4": {"title": "Goats", "alternative_codes": ["4B4", "4 B 4"]},
        "4.B.5": {"title": "Camels and Llamas", "alternative_codes": ["4B5", "4 B 5"]},
        "4.B.6": {"title": "Horses", "alternative_codes": ["4B6", "4 B 6"]},
        "4.B.7": {"title": "Mules and Asses", "alternative_codes": ["4B7", "4 B 7"]},
        "4.B.8": {"title": "Swine", "alternative_codes": ["4B8", "4 B 8"]},
        "4.B.9": {"title": "Poultry", "alternative_codes": ["4B9", "4 B 9"]},
        "4.B.10": {
            "title": "Anaerobic Lagoons",
            "alternative_codes": ["4B10", "4 B 10"],
        },
        "4.B.11": {"title": "Liquid Systems", "alternative_codes": ["4B11", "4 B 11"]},
        "4.B.12": {
            "title": "Solid Storage and Drylot",
            "alternative_codes": ["4B12", "4 B 12"],
        },
        "4.B.13": {
            "title": "Other",
            "comment": "Please specify.",
            "alternative_codes": ["4B13", "4 B 13"],
        },
        "4.C": {
            "title": "Rice Cultivation",
            "comment": "The anaerobic decomposition of organic material in flooded rice fields produces methane, which escapes to the atmosphere by ebullition (bubbling up) through the water column, diffusion across the water/air interface, and transport through the rice plants. It is suggested that these CH4 emissions be based on lowland rice ecosystems without organic amendments relating to water regime, where lowland refers to fields flooded for a significant period of time. Correction factors for soils with organic amendments from the use of should be applied as necessary. Any N2O emissions nitrogen-based fertilisers in rice cultivation should be reported under 4 D Agricultural Soils.",
            "alternative_codes": ["4C", "4 C"],
            "children": [["4.C.1", "4.C.2", "4.C.3", "4.C.4"]],
        },
        "4.C.1": {
            "title": "Irrigated",
            "comment": "Water regime is fully controlled.",
            "alternative_codes": ["4C1", "4 C 1"],
            "children": [["4.C.1.a", "4.C.1.b"]],
        },
        "4.C.1.a": {
            "title": "Continuously Flooded",
            "alternative_codes": ["4C1a", "4 C 1 a"],
        },
        "4.C.1.b": {
            "title": "Intermittently Flooded",
            "alternative_codes": ["4C1b", "4 C 1 b"],
            "children": [["4.C.1.b.i", "4.C.1.b.ii"]],
        },
        "4.C.1.b.i": {
            "title": "Single Aeration",
            "comment": "Fields have a single aeration during the cropping season at any growth stage.",
            "alternative_codes": ["4C1bi", "4 C 1 b i"],
        },
        "4.C.1.b.ii": {
            "title": "Multiple Aeration",
            "comment": "Fields have more than one aeration period during the cropping season.",
            "alternative_codes": ["4C1bii", "4 C 1 b ii"],
        },
        "4.C.2": {
            "title": "Rainfed",
            "comment": "Water regime depends solely on precipitation.",
            "alternative_codes": ["4C2", "4 C 2"],
            "children": [["4.C.2.a", "4.C.2.b"]],
        },
        "4.C.2.a": {
            "title": "Flood Prone",
            "comment": "The water level may rise up to 50 cm during the cropping season.",
            "alternative_codes": ["4C2a", "4 C 2 a"],
        },
        "4.C.2.b": {
            "title": "Drought Prone",
            "comment": "Drought periods occur during every cropping season.",
            "alternative_codes": ["4C2b", "4 C 2 b"],
        },
        "4.C.3": {
            "title": "Deepwater",
            "comment": "Floodwater rises to more than 50 cm for a significant period of time during the cropping season.",
            "alternative_codes": ["4C3", "4 C 3"],
            "children": [["4.C.3.a", "4.C.3.b"]],
        },
        "4.C.3.a": {
            "title": "Water Depth 50-100 cm",
            "comment": "Fields inundated with water depth from 50 100 cm.",
            "alternative_codes": ["4C3a", "4 C 3 a"],
        },
        "4.C.3.b": {
            "title": "Water Depth > 100 cm",
            "comment": "Fields inundated with water depth 100 cm.",
            "alternative_codes": ["4C3b", "4 C 3 b"],
        },
        "4.C.4": {"title": "Other", "alternative_codes": ["4C4", "4 C 4"]},
        "4.D": {
            "title": "Agricultural Soils",
            "comment": "Emissions and removals of CH4 and N2O from agricultural soil/land and NMVOCs from crops. These are influenced by irrigation practices, climatic variables, soil temperature and humidity. Any N2O emissions from the use of nitrogen-based fertilisers in rice cultivation should be reported here. N2O emissions may be related to the use of both organic and inorganic fertilisers, biological Nitrogen fixation, and return of crop residues to the field or to animal production. Non-CO2 greenhouse gas emissions associated with the use of compost and human waste as fertilisers should also be recorded in this category. Emissions of N2O from sewage are to be reported under Waste from animal waste (6 B) and N2O emissions management systems other than grazing under manure management (4 B). Emissions of N2O from manure used for fuel are reported under the Energy Module (1 A).",
            "alternative_codes": ["4D", "4 D"],
            "children": [["4.D.1", "4.D.2", "4.D.3", "4.D.4"]],
        },
        "4.E": {
            "title": "Prescribed Burning of Savannas",
            "comment": "Emissions of CH4, CO, N2O, and NOx from the burning of savannas*. Savannas are burned to control the growth of vegetation, remove pests and weeds, promote the nutrient cycle and to encourage the growth of new grass for animal grazing. CO2 from savanna burning is noted for information but is not included in the inventory total since it is assumed that an equivalent amount of CO2 is removed by regrowing vegetation in the following year. *Savannas are tropical and subtropical formations with continuous grass cover, occasionally interrupted by trees and shrubs, which exist in Africa, Latin America, Asia, and Australia.",
            "alternative_codes": ["4E", "4 E"],
        },
        "4.F": {
            "title": "Field Burning of Agricultural Residues",
            "comment": "Emission of non-CO2 greenhouse gases from burning (in the field) of crop residue and other agricultural wastes on site. These include woody crop residues (e.g. coconut shells, jute sticks, etc.); cereal residues (e.g. rice and wheat straw, maize stalks, etc.); green crop residues (e.g. groundnut straw, soybean tops, etc.). The burning of agricultural waste for energy is excluded here but included under fuel combustion activities in Section 1 A. CO2 from vegetal or biomass burning is noted for information but is not included in the inventory total, since it is assumed that a roughly equivalent amount of CO2 is removed by regrowth of the next crop.",
            "alternative_codes": ["4F", "4 F"],
            "children": [["4.F.1", "4.F.2", "4.F.3", "4.F.4", "4.F.5"]],
        },
        "4.F.1": {
            "title": "Cereals",
            "comment": "Emissions from the on-site burning of residue from cereal crops harvested for dry grain, including but not limited to wheat, barley, maize, oats, rye, rice, millet and sorghum.",
            "alternative_codes": ["4F1", "4 F 1"],
            "children": [
                [
                    "4.F.1.a",
                    "4.F.1.b",
                    "4.F.1.c",
                    "4.F.1.d",
                    "4.F.1.e",
                    "4.F.1.f",
                    "4.F.1.g",
                ]
            ],
        },
        "4.F.2": {
            "title": "Pulse",
            "comment": "Emissions from the on-site burning of residue from pulse crops harvested for dry grain, including but not limited to pea, bean and soya.",
            "alternative_codes": ["4F2", "4 F 2"],
            "children": [["4.F.2.a", "4.F.2.b", "4.F.2.c", "4.F.2.d"]],
        },
        "4.F.3": {
            "title": "Tuber and Root",
            "comment": "Emissions from the on-site burning of residue from tuber and root crops, including but not limited to potatoes, feedbeet, sugarbeet, girasol (Jerusalem artichoke) and peanut.",
            "alternative_codes": ["4F3", "4 F 3"],
            "children": [["4.F.3.a", "4.F.3.b"]],
        },
        "4.F.4": {
            "title": "Sugar Cane",
            "comment": "Emissions from the on-site burning of sugar cane crop residue.",
            "alternative_codes": ["4F4", "4 F 4"],
        },
        "4.F.5": {
            "title": "Other",
            "comment": "Emissions from the on-site burning of residue from crops not included above.",
            "alternative_codes": ["4F5", "4 F 5"],
        },
        "4.G": {
            "title": "Other",
            "comment": "Describe each emission source/sink in detail.",
            "alternative_codes": ["4G", "4 G"],
        },
        "5": {
            "title": "Land-Use Change & Forestry",
            "comment": "Total emissions and removals from forest and land use change activities as described below. These activities have an impact on three different carbon sources/sinks: aboveground biomass, belowground biomass and soil carbon. Sum of 5 A, B, C, D & E.",
            "children": [["5.A", "5.B", "5.C", "5.D", "5.E"]],
        },
        "5.B": {
            "title": "Forest and Grassland Conversion",
            "comment": "This category includes conversion of existing forests and natural grasslands to other land uses. Emissions of CO2, CH4, CO, N2O, NOx and NMVOCs from the burning and decay of biomass.",
            "alternative_codes": ["5B", "5 B"],
            "children": [
                ["5.B-gra", "5.B-tro", "5.B.1", "5.B.2", "5.B.3", "5.B.4", "5.B.5"]
            ],
        },
        "5.B.1": {
            "title": "Tropical Forests",
            "alternative_codes": ["5B1", "5 B 1"],
            "children": [
                [
                    "5.B.1.a",
                    "5.B.1.b",
                    "5.B.1.c",
                    "5.B.1.d",
                    "5.B.1.e",
                    "5.B.1.f",
                    "5.B.1.g",
                    "5.B.1.h",
                ]
            ],
        },
        "5.B.1.a": {
            "title": "Wet/Very Moist",
            "alternative_codes": ["5B1a", "5 B 1 a"],
        },
        "5.B.1.b": {
            "title": "Moist, Short Dry Season",
            "alternative_codes": ["5B1b", "5 B 1 b"],
        },
        "5.B.1.c": {
            "title": "Moist, Long Dry Season",
            "alternative_codes": ["5B1c", "5 B 1 c"],
        },
        "5.B.1.d": {"title": "Dry", "alternative_codes": ["5B1d", "5 B 1 d"]},
        "5.B.1.e": {
            "title": "Mountain Moist",
            "alternative_codes": ["5B1e", "5 B 1 e"],
        },
        "5.B.1.f": {"title": "Mountain Dry", "alternative_codes": ["5B1f", "5 B 1 f"]},
        "5.B.1.g": {"title": "Plantations", "alternative_codes": ["5B1g", "5 B 1 g"]},
        "5.B.1.h": {"title": "Other", "alternative_codes": ["5B1h", "5 B 1 h"]},
        "5.B.2": {
            "title": "Temperate Forests",
            "alternative_codes": ["5B2", "5 B 2"],
            "children": [["5.B.2-mix", "5.B.2.a", "5.B.2.b", "5.B.2.c", "5.B.2.d"]],
        },
        "5.B.2.a": {"title": "Coniferous", "alternative_codes": ["5B2a", "5 B 2 a"]},
        "5.B.2.b": {"title": "Broadleaf", "alternative_codes": ["5B2b", "5 B 2 b"]},
        "5.B.2.c": {"title": "Plantations", "alternative_codes": ["5B2c", "5 B 2 c"]},
        "5.B.2.d": {"title": "Other", "alternative_codes": ["5B2d", "5 B 2 d"]},
        "5.B.3": {
            "title": "Boreal Forests",
            "alternative_codes": ["5B3", "5 B 3"],
            "children": [["5.B.3.a", "5.B.3.b", "5.B.3.c"]],
        },
        "5.B.3.a": {
            "title": "Mixed Broadleaf/Coniferous",
            "alternative_codes": ["5B3a", "5 B 3 a"],
        },
        "5.B.3.b": {"title": "Coniferous", "alternative_codes": ["5B3b", "5 B 3 b"]},
        "5.B.3.c": {"title": "Forest Tundra", "alternative_codes": ["5B3c", "5 B 3 c"]},
        "5.B.4": {
            "title": "Grasslands/Tundra",
            "comment": "Emissions of CO2 from grasslands including tropical savanna and boreal tundra.",
            "alternative_codes": ["5B4", "5 B 4"],
        },
        "5.B.5": {
            "title": "Other",
            "comment": "Emissions from conversion of ecosystem types (e.g. wastelands, desert, etc.) not otherwise covered in any of the above categories.",
            "alternative_codes": ["5B5", "5 B 5"],
        },
        "5.C": {
            "title": "Abandonment of Managed Lands",
            "comment": "Removal of CO2 from the abandonment of formerly managed lands (e.g. croplands and pastures). This category includes conversion of managed to abandoned lands. The categories below are determined by the type of biomass which regrows on the abandoned land.",
            "alternative_codes": ["5C", "5 C"],
            "children": [
                ["5.C-gra", "5.C-tro", "5.C.1", "5.C.2", "5.C.3", "5.C.4", "5.C.5"]
            ],
        },
        "5.C.1": {
            "title": "Tropical Forests",
            "alternative_codes": ["5C1", "5 C 1"],
            "children": [
                ["5.C.1.a", "5.C.1.b", "5.C.1.c", "5.C.1.d", "5.C.1.e", "5.C.1.f"]
            ],
        },
        "5.C.2": {
            "title": "Temperate Forests",
            "alternative_codes": ["5C2", "5 C 2"],
            "children": [["5.C.2.a", "5.C.2.b", "5.C.2.c"]],
        },
        "5.C.3": {
            "title": "Boreal Forests",
            "alternative_codes": ["5C3", "5 C 3"],
            "children": [["5.C.3.a", "5.C.3.b", "5.C.3.c"]],
        },
        "5.C.4": {"title": "Grasslands/Tundra", "alternative_codes": ["5C4", "5 C 4"]},
        "5.C.5": {
            "title": "Other",
            "comment": "Removals from abandoned land regrown to any biomass type other than forests or grasslands.",
            "alternative_codes": ["5C5", "5 C 5"],
        },
        "5.D": {
            "title": "CO2 Emissions and Removals From Soil",
            "comment": "Emissions and removals of CO2 in soil associated with land-use change and management. Includes CO2 emissions from liming of agricultural soil.",
            "alternative_codes": ["5D", "5 D"],
            "children": [["5.D.1", "5.D.2", "5.D.3", "5.D.4", "5.D.5"]],
        },
        "5.E": {
            "title": "Other",
            "comment": "Emissions and removals (sources and sinks) of CO2 from land use or land-use change activities which can not be included under the categories provided above. Emissions of NMVOC from the living trees in managed forests and N2O or CH4 emissions/removals from the soil of managed forests are reported here. Managed forests include all trees planted or managed by man for profit, pleasure, wind or water-erosion protection etc.",
            "alternative_codes": ["5E", "5 E"],
        },
        "6": {
            "title": "Waste",
            "comment": "Total emissions from solid waste disposal on land, wastewater, waste incineration and any other waste management activity. Any emissions from fossil-based products (incineration or CO2 decomposition) should be accounted for here but see note on double counting under Section 2 “Reporting the National Inventory.” CO2 from organic waste handling and decay should not be included (see below). Sum of 6 A, B, C & D.",
            "children": [["6.A", "6.B", "6.C", "6.D"]],
        },
        "6.A": {
            "title": "Solid Waste Disposal on Land",
            "comment": "Methane is produced from anaerobic microbial decomposition of organic matter in solid waste disposal sites. Carbon dioxide from non-biologic or (CO2) is also produced but only CO2 inorganic waste sources should be reported here.",
            "alternative_codes": ["6A", "6 A"],
            "children": [["6.A.1", "6.A.2", "6.A.3"]],
        },
        "6.A.1": {
            "title": "Managed Waste Disposal on Land",
            "comment": "A managed solid waste disposal site must have controlled placement of waste (i.e. waste directed to specific deposition areas, a degree of control of scavenging and a degree of control fires) and will include at least one of the following: cover material; mechanical compaction; or levelling of the waste.",
            "alternative_codes": ["6A1", "6 A 1"],
        },
        "6.A.2": {
            "title": "Unmanaged Waste Disposal Sites",
            "comment": "These are all other solid waste disposal sites that do not fall into the above category.",
            "alternative_codes": ["6A2", "6 A 2"],
            "children": [["6.A.2.a", "6.A.2.b"]],
        },
        "6.A.3": {
            "title": "Other",
            "comment": "Other solid waste disposal on land.",
            "alternative_codes": ["6A3", "6 A 3"],
        },
        "6.B": {
            "title": "Wastewater Handling",
            "comment": "Methane and nitrous oxide are produced from anaerobic decomposition of organic matter by bacteria in sewage facilities and from food processing and other industrial facilities during wastewater handling. N2O may also be released from wastewater handling and human waste. Methane emissions are covered in 6 B 1 and 6 B 2, nitrous oxide emissions in 6 B 2.",
            "alternative_codes": ["6B", "6 B"],
            "children": [["6.B.1", "6.B.2", "6.B.3"]],
        },
        "6.B.1": {
            "title": "Industrial Wastewater",
            "comment": "Handling of liquid wastes and sludge from industrial processes such as: food processing, textiles, or pulp and paper production. This may involve such things as wastewater collection and treatment, ponds, or discharge into surface water.",
            "alternative_codes": ["6B1", "6 B 1"],
        },
        "6.B.2": {
            "title": "Domestic and Commercial Wastewater",
            "comment": "Handling of liquid wastes and sludge from housing and commercial sources (including human waste) through: wastewater collection and treatment, open pits / latrines, ponds, or discharge into surface waters. N2O emissions from discharge of human sewage to aquatic environments are included here.",
            "alternative_codes": ["6B2", "6 B 2"],
        },
        "6.B.3": {"title": "Other", "alternative_codes": ["6B3", "6 B 3"]},
        "6.C": {
            "title": "Waste Incineration",
            "comment": "Incineration of waste, not including waste-to-energy facilities. Emissions from waste burnt for energy are reported under the Energy Module, 1 A. Emissions from burning of agricultural wastes should be reported under Section 4. All non-CO2 greenhouse gases from incineration should be reported here as well as CO2 from non-biological waste.",
            "alternative_codes": ["6C", "6 C"],
            "children": [["6.C.1", "6.C.2", "6.C.3"]],
        },
        "6.D": {
            "title": "Other",
            "comment": "Release of greenhouse gases from other waste handling activities.",
            "alternative_codes": ["6D", "6 D"],
        },
        "7": {
            "title": "Other",
            "comment": "Efforts should be made to fit all emission sources/sinks into the six categories described above. If it is impossible to do so, however, this category may be used, accompanied by a detailed explanation of the source/sink activity.",
        },
        "2.F.8": {
            "title": "Other",
            "comment": "Please specify.",
            "alternative_codes": ["2F8", "2 F 8"],
        },
        "1.A-ref": {
            "title": "Reference Approach",
            "alternative_codes": ["1 A-ref", "1A-ref"],
            "children": [["1.A-ref.1", "1.A-ref.2"]],
        },
        "1.A-ref.1": {
            "title": "Fossil Fuel",
            "alternative_codes": ["1 A-ref 1", "1A-ref1"],
            "children": [["1.A-ref.1.a", "1.A-ref.1.b", "1.A-ref.1.c"]],
        },
        "1.A-ref.1.a": {
            "title": "Liquid Fossil",
            "alternative_codes": ["1 A-ref 1 a", "1A-ref1a"],
            "children": [["1.A-ref.1.a.i", "1.A-ref.1.a.ii"]],
        },
        "1.A-ref.1.a.i": {
            "title": "Primary Fuels",
            "alternative_codes": ["1 A-ref 1 a i", "1A-ref1ai"],
            "children": [["1.A-ref.1.a.i.1", "1.A-ref.1.a.i.2", "1.A-ref.1.a.i.3"]],
        },
        "1.A-ref.1.a.i.1": {
            "title": "Crude Oil",
            "alternative_codes": ["1 A-ref 1 a i 1", "1A-ref1ai1"],
        },
        "1.A-ref.1.a.i.2": {
            "title": "Orimulsion",
            "alternative_codes": ["1 A-ref 1 a i 2", "1A-ref1ai2"],
        },
        "1.A-ref.1.a.i.3": {
            "title": "Natural Gas Liquids",
            "alternative_codes": ["1 A-ref 1 a i 3", "1A-ref1ai3"],
        },
        "1.A-ref.1.a.ii": {
            "title": "Secondary Fuels",
            "alternative_codes": ["1 A-ref 1 a ii", "1A-ref1aii"],
            "children": [
                [
                    "1.A-ref.1.a.ii.1",
                    "1.A-ref.1.a.ii.10",
                    "1.A-ref.1.a.ii.11",
                    "1.A-ref.1.a.ii.12",
                    "1.A-ref.1.a.ii.13",
                    "1.A-ref.1.a.ii.14",
                    "1.A-ref.1.a.ii.2",
                    "1.A-ref.1.a.ii.3",
                    "1.A-ref.1.a.ii.4",
                    "1.A-ref.1.a.ii.5",
                    "1.A-ref.1.a.ii.6",
                    "1.A-ref.1.a.ii.7",
                    "1.A-ref.1.a.ii.8",
                    "1.A-ref.1.a.ii.9",
                ]
            ],
        },
        "1.A-ref.1.a.ii.1": {
            "title": "Gasoline",
            "alternative_codes": ["1 A-ref 1 a ii 1", "1A-ref1aii1"],
        },
        "1.A-ref.1.a.ii.2": {
            "title": "Jet Kerosene",
            "alternative_codes": ["1 A-ref 1 a ii 2", "1A-ref1aii2"],
        },
        "1.A-ref.1.a.ii.3": {
            "title": "Other Kerosene",
            "alternative_codes": ["1 A-ref 1 a ii 3", "1A-ref1aii3"],
        },
        "1.A-ref.1.a.ii.4": {
            "title": "Shale Oil",
            "alternative_codes": ["1 A-ref 1 a ii 4", "1A-ref1aii4"],
        },
        "1.A-ref.1.a.ii.5": {
            "title": "Gas / Diesel Oil",
            "alternative_codes": ["1 A-ref 1 a ii 5", "1A-ref1aii5"],
        },
        "1.A-ref.1.a.ii.6": {
            "title": "Residual Fuel Oil",
            "alternative_codes": ["1 A-ref 1 a ii 6", "1A-ref1aii6"],
        },
        "1.A-ref.1.a.ii.7": {
            "title": "LPG",
            "alternative_codes": ["1 A-ref 1 a ii 7", "1A-ref1aii7"],
        },
        "1.A-ref.1.a.ii.8": {
            "title": "Ethane",
            "alternative_codes": ["1 A-ref 1 a ii 8", "1A-ref1aii8"],
        },
        "1.A-ref.1.a.ii.9": {
            "title": "Naphtha",
            "alternative_codes": ["1 A-ref 1 a ii 9", "1A-ref1aii9"],
        },
        "1.A-ref.1.a.ii.10": {
            "title": "Bitumen",
            "alternative_codes": ["1 A-ref 1 a ii 10", "1A-ref1aii10"],
        },
        "1.A-ref.1.a.ii.11": {
            "title": "Lubricants",
            "alternative_codes": ["1 A-ref 1 a ii 11", "1A-ref1aii11"],
        },
        "1.A-ref.1.a.ii.12": {
            "title": "Petroleum Coke",
            "alternative_codes": ["1 A-ref 1 a ii 12", "1A-ref1aii12"],
        },
        "1.A-ref.1.a.ii.13": {
            "title": "Refinery Feedstocks",
            "alternative_codes": ["1 A-ref 1 a ii 13", "1A-ref1aii13"],
        },
        "1.A-ref.1.a.ii.14": {
            "title": "Other Oil",
            "alternative_codes": ["1 A-ref 1 a ii 14", "1A-ref1aii14"],
        },
        "1.A-ref.1.b": {
            "title": "Solid Fossil",
            "alternative_codes": ["1 A-ref 1 b", "1A-ref1b"],
            "children": [["1.A-ref.1.b.i", "1.A-ref.1.b.ii"]],
        },
        "1.A-ref.1.b.i": {
            "title": "Primary Fuels",
            "alternative_codes": ["1 A-ref 1 b i", "1A-ref1bi"],
            "children": [
                [
                    "1.A-ref.1.b.i.1",
                    "1.A-ref.1.b.i.2",
                    "1.A-ref.1.b.i.3",
                    "1.A-ref.1.b.i.4",
                    "1.A-ref.1.b.i.5",
                    "1.A-ref.1.b.i.6",
                    "1.A-ref.1.b.i.7",
                ]
            ],
        },
        "1.A-ref.1.b.i.1": {
            "title": "Anthracite",
            "alternative_codes": ["1 A-ref 1 b i 1", "1A-ref1bi1"],
        },
        "1.A-ref.1.b.i.2": {
            "title": "Coking Coal",
            "alternative_codes": ["1 A-ref 1 b i 2", "1A-ref1bi2"],
        },
        "1.A-ref.1.b.i.3": {
            "title": "Other Bituminous Coal",
            "alternative_codes": ["1 A-ref 1 b i 3", "1A-ref1bi3"],
        },
        "1.A-ref.1.b.i.4": {
            "title": "Sub-bituminous coal",
            "alternative_codes": ["1 A-ref 1 b i 4", "1A-ref1bi4"],
        },
        "1.A-ref.1.b.i.5": {
            "title": "Lignite",
            "alternative_codes": ["1 A-ref 1 b i 5", "1A-ref1bi5"],
        },
        "1.A-ref.1.b.i.6": {
            "title": "Oil Shale",
            "alternative_codes": ["1 A-ref 1 b i 6", "1A-ref1bi6"],
        },
        "1.A-ref.1.b.i.7": {
            "title": "Peat",
            "alternative_codes": ["1 A-ref 1 b i 7", "1A-ref1bi7"],
        },
        "1.A-ref.1.b.ii": {
            "title": "Secondary Fuels",
            "alternative_codes": ["1 A-ref 1 b ii", "1A-ref1bii"],
            "children": [["1.A-ref.1.b.ii.1", "1.A-ref.1.b.ii.2"]],
        },
        "1.A-ref.1.b.ii.1": {
            "title": "BKB & Patent Fuel",
            "alternative_codes": ["1 A-ref 1 b ii 1", "1A-ref1bii1"],
        },
        "1.A-ref.1.b.ii.2": {
            "title": "Coke Oven / Gas Coke",
            "alternative_codes": ["1 A-ref 1 b ii 2", "1A-ref1bii2"],
        },
        "1.A-ref.1.c": {
            "title": "Gaseous Fossil",
            "alternative_codes": ["1 A-ref 1 c", "1A-ref1c"],
            "children": [["1.A-ref.1.c.i"]],
        },
        "1.A-ref.1.c.i": {
            "title": "Natural Gas (Dry)",
            "alternative_codes": ["1 A-ref 1 c i", "1A-ref1ci"],
        },
        "1.A-ref.2": {
            "title": "Biomass",
            "alternative_codes": ["1 A-ref 2", "1A-ref2"],
            "children": [["1.A-ref.2.a", "1.A-ref.2.b", "1.A-ref.2.c"]],
        },
        "1.A-ref.2.a": {
            "title": "Solid Biomass",
            "alternative_codes": ["1 A-ref 2 a", "1A-ref2a"],
        },
        "1.A-ref.2.b": {
            "title": "Liquid Biomass",
            "alternative_codes": ["1 A-ref 2 b", "1A-ref2b"],
        },
        "1.A-ref.2.c": {
            "title": "Gas Biomass",
            "alternative_codes": ["1 A-ref 2 c", "1A-ref2c"],
        },
        "1.B.2.b-exp": {
            "title": "Exploration",
            "alternative_codes": ["1 B 2 b-exp", "1B2b-exp"],
        },
        "1.B.2.b-dis": {
            "title": "Distribution",
            "alternative_codes": ["1 B 2 b-dis", "1B2b-dis"],
        },
        "1.B.2.b.iii.1": {
            "title": "at industrial plants and power stations",
            "alternative_codes": ["1 B 2 b iii 1", "1B2biii1"],
        },
        "1.B.2.b.iii.2": {
            "title": "in residential and commercial sectors",
            "alternative_codes": ["1 B 2 b iii 2", "1B2biii2"],
        },
        "1.B.2.c-ven": {
            "title": "Venting",
            "alternative_codes": ["1 B 2 c-ven", "1B2c-ven"],
            "children": [["1.B.2.c-ven.i", "1.B.2.c-ven.ii", "1.B.2.c-ven.iii"]],
        },
        "1.B.2.c-ven.i": {
            "title": "Oil",
            "alternative_codes": ["1 B 2 c-ven i", "1B2c-veni"],
        },
        "1.B.2.c-ven.ii": {
            "title": "Gas",
            "alternative_codes": ["1 B 2 c-ven ii", "1B2c-venii"],
        },
        "1.B.2.c-ven.iii": {
            "title": "Combined",
            "alternative_codes": ["1 B 2 c-ven iii", "1B2c-veniii"],
        },
        "1.B.2.c-fla": {
            "title": "Flaring",
            "alternative_codes": ["1 B 2 c-fla", "1B2c-fla"],
            "children": [["1.B.2.c-fla.i", "1.B.2.c-fla.ii", "1.B.2.c-fla.iii"]],
        },
        "1.B.2.c-fla.i": {
            "title": "Oil",
            "alternative_codes": ["1 B 2 c-fla i", "1B2c-flai"],
        },
        "1.B.2.c-fla.ii": {
            "title": "Gas",
            "alternative_codes": ["1 B 2 c-fla ii", "1B2c-flaii"],
        },
        "1.B.2.c-fla.iii": {
            "title": "Combined",
            "alternative_codes": ["1 B 2 c-fla iii", "1B2c-flaiii"],
        },
        "1.B.2.d": {"title": "Other", "alternative_codes": ["1 B 2 d", "1B2d"]},
        "2.E.1.a": {
            "title": "Production of HCFC-22",
            "alternative_codes": ["2 E 1 a", "2E1a"],
        },
        "2.E.1.b": {"title": "Other", "alternative_codes": ["2 E 1 b", "2E1b"]},
        "2.F.6": {
            "title": "Semiconductor Manufacture",
            "alternative_codes": ["2 F 6", "2F6"],
        },
        "2.F.7": {
            "title": "Electrical Equipment",
            "alternative_codes": ["2 F 7", "2F7"],
        },
        "2.A.7.a": {
            "title": "Glass Production",
            "alternative_codes": ["2 A 7 a", "2A7a"],
        },
        "2.A.7.b": {"title": "Other", "alternative_codes": ["2 A 7 b", "2A7b"]},
        "2.B.4.a": {
            "title": "Silicon Carbide",
            "alternative_codes": ["2 B 4 a", "2B4a"],
        },
        "2.B.4.b": {
            "title": "Calcium Carbide",
            "alternative_codes": ["2 B 4 b", "2B4b"],
        },
        "2.B.5.a": {"title": "Carbon Black", "alternative_codes": ["2 B 5 a", "2B5a"]},
        "2.B.5.b": {"title": "Ethylene", "alternative_codes": ["2 B 5 b", "2B5b"]},
        "2.B.5.c": {
            "title": "Dichloroethylene",
            "alternative_codes": ["2 B 5 c", "2B5c"],
        },
        "2.B.5.d": {"title": "Styrene", "alternative_codes": ["2 B 5 d", "2B5d"]},
        "2.B.5.e": {"title": "Methanol", "alternative_codes": ["2 B 5 e", "2B5e"]},
        "2.B.5.f": {"title": "Other", "alternative_codes": ["2 B 5 f", "2B5f"]},
        "2.C.1.a": {"title": "Steel", "alternative_codes": ["2 C 1 a", "2C1a"]},
        "2.C.1.b": {"title": "Pig Iron", "alternative_codes": ["2 C 1 b", "2C1b"]},
        "2.C.1.c": {"title": "Sinter", "alternative_codes": ["2 C 1 c", "2C1c"]},
        "2.C.1.d": {"title": "Coke", "alternative_codes": ["2 C 1 d", "2C1d"]},
        "2.C.1.e": {"title": "Other", "alternative_codes": ["2 C 1 e", "2C1e"]},
        "2.C.4.a": {
            "title": "SF6 used in Aluminium Foundries",
            "alternative_codes": ["2 C 4 a", "2C4a"],
        },
        "2.C.4.b": {
            "title": "SF6 used in Magnesium Foundries",
            "alternative_codes": ["2 C 4 b", "2C4b"],
        },
        "2.F.1.a": {
            "title": "Domestic Refrigeration",
            "alternative_codes": ["2 F 1 a", "2F1a"],
        },
        "2.F.1.b": {
            "title": "Commercial Refrigeration",
            "alternative_codes": ["2 F 1 b", "2F1b"],
        },
        "2.F.1.c": {
            "title": "Transport Refrigeration",
            "alternative_codes": ["2 F 1 c", "2F1c"],
        },
        "2.F.1.d": {
            "title": "Industrial Refrigeration",
            "alternative_codes": ["2 F 1 d", "2F1d"],
        },
        "2.F.1.e": {
            "title": "Stationary Air-Conditioning",
            "alternative_codes": ["2 F 1 e", "2F1e"],
        },
        "2.F.1.f": {
            "title": "Mobile Air-Conditioning",
            "alternative_codes": ["2 F 1 f", "2F1f"],
        },
        "2.F.2.a": {"title": "Hard Foam", "alternative_codes": ["2 F 2 a", "2F2a"]},
        "2.F.2.b": {"title": "Soft Foam", "alternative_codes": ["2 F 2 b", "2F2b"]},
        "2.F.4.a": {
            "title": "Metered Dose Inhalers",
            "alternative_codes": ["2 F 4 a", "2F4a"],
        },
        "2.F.4.b": {"title": "Other", "alternative_codes": ["2 F 4 b", "2F4b"]},
        "3.D.1": {
            "title": "Use of N2O for Anaesthesia",
            "alternative_codes": ["3 D 1", "3D1"],
        },
        "3.D.2": {
            "title": "N2O from Fire Extinguishers",
            "alternative_codes": ["3 D 2", "3D2"],
        },
        "3.D.3": {
            "title": "N2O from Aerosol Cans",
            "alternative_codes": ["3 D 3", "3D3"],
        },
        "3.D.4": {"title": "Other Use of N2O", "alternative_codes": ["3 D 4", "3D4"]},
        "3.D.5": {"title": "Other", "alternative_codes": ["3 D 5", "3D5"]},
        "4.D.1": {
            "title": "Direct Soil Emissions",
            "alternative_codes": ["4 D 1", "4D1"],
            "children": [["4.D.1.a", "4.D.1.b", "4.D.1.c", "4.D.1.d", "4.D.1.e"]],
        },
        "4.D.1.a": {
            "title": "Synthetic Fertilizers",
            "alternative_codes": ["4 D 1 a", "4D1a"],
        },
        "4.D.1.b": {
            "title": "Animal Wastes Applied to Soils",
            "alternative_codes": ["4 D 1 b", "4D1b"],
        },
        "4.D.1.c": {
            "title": "N-fixing Crops",
            "alternative_codes": ["4 D 1 c", "4D1c"],
        },
        "4.D.1.d": {"title": "Crop Residue", "alternative_codes": ["4 D 1 d", "4D1d"]},
        "4.D.1.e": {
            "title": "Cultivation of Histosols",
            "alternative_codes": ["4 D 1 e", "4D1e"],
        },
        "4.D.2": {"title": "Animal Production", "alternative_codes": ["4 D 2", "4D2"]},
        "4.D.3": {
            "title": "Indirect Emissions",
            "alternative_codes": ["4 D 3", "4D3"],
            "children": [["4.D.3.a", "4.D.3.b"]],
        },
        "4.D.3.a": {
            "title": "Atmospheric Deposition",
            "alternative_codes": ["4 D 3 a", "4D3a"],
        },
        "4.D.3.b": {
            "title": "Nitrogen Leaching and Run-off",
            "alternative_codes": ["4 D 3 b", "4D3b"],
        },
        "4.D.4": {"title": "Other", "alternative_codes": ["4 D 4", "4D4"]},
        "4.F.1.a": {"title": "Wheat", "alternative_codes": ["4 F 1 a", "4F1a"]},
        "4.F.1.b": {"title": "Barley", "alternative_codes": ["4 F 1 b", "4F1b"]},
        "4.F.1.c": {"title": "Maize", "alternative_codes": ["4 F 1 c", "4F1c"]},
        "4.F.1.d": {"title": "Oats", "alternative_codes": ["4 F 1 d", "4F1d"]},
        "4.F.1.e": {"title": "Rye", "alternative_codes": ["4 F 1 e", "4F1e"]},
        "4.F.1.f": {"title": "Rice", "alternative_codes": ["4 F 1 f", "4F1f"]},
        "4.F.1.g": {"title": "Other", "alternative_codes": ["4 F 1 g", "4F1g"]},
        "4.F.2.a": {"title": "Dry bean", "alternative_codes": ["4 F 2 a", "4F2a"]},
        "4.F.2.b": {"title": "Peas", "alternative_codes": ["4 F 2 b", "4F2b"]},
        "4.F.2.c": {"title": "Soybeans", "alternative_codes": ["4 F 2 c", "4F2c"]},
        "4.F.2.d": {"title": "Other", "alternative_codes": ["4 F 2 d", "4F2d"]},
        "4.F.3.a": {"title": "Potatoes", "alternative_codes": ["4 F 3 a", "4F3a"]},
        "4.F.3.b": {"title": "Other", "alternative_codes": ["4 F 3 b", "4F3b"]},
        "5.A": {
            "title": "Changes in Forest and Other Woody Biomass Stocks",
            "alternative_codes": ["5 A", "5A"],
            "children": [["5.A.1", "5.A.2", "5.A.3", "5.A.4", "5.A.5"]],
        },
        "5.A.1": {
            "title": "Tropical",
            "alternative_codes": ["5 A 1", "5A1"],
            "children": [["5.A.1.a", "5.A.1.b", "5.A.1.c"]],
        },
        "5.A.1.a": {
            "title": "Plantations",
            "alternative_codes": ["5 A 1 a", "5A1a"],
            "children": [
                [
                    "5.A.1.a.i",
                    "5.A.1.a.ii",
                    "5.A.1.a.iii",
                    "5.A.1.a.iv",
                    "5.A.1.a.ix",
                    "5.A.1.a.v",
                    "5.A.1.a.vi",
                    "5.A.1.a.vii",
                    "5.A.1.a.viii",
                ]
            ],
        },
        "5.A.1.a.i": {
            "title": "Acacia spp.",
            "alternative_codes": ["5 A 1 a i", "5A1ai"],
        },
        "5.A.1.a.ii": {
            "title": "Eucalyptus spp.",
            "alternative_codes": ["5 A 1 a ii", "5A1aii"],
        },
        "5.A.1.a.iii": {
            "title": "Tectona grandis",
            "alternative_codes": ["5 A 1 a iii", "5A1aiii"],
        },
        "5.A.1.a.iv": {
            "title": "Pinus spp",
            "alternative_codes": ["5 A 1 a iv", "5A1aiv"],
        },
        "5.A.1.a.v": {
            "title": "Pinus caribaea",
            "alternative_codes": ["5 A 1 a v", "5A1av"],
        },
        "5.A.1.a.vi": {
            "title": "Mixed Hardwoods",
            "alternative_codes": ["5 A 1 a vi", "5A1avi"],
        },
        "5.A.1.a.vii": {
            "title": "Mixed Fast-Growing Hardwoods",
            "alternative_codes": ["5 A 1 a vii", "5A1avii"],
        },
        "5.A.1.a.viii": {
            "title": "Mixed Softwoods",
            "alternative_codes": ["5 A 1 a viii", "5A1aviii"],
        },
        "5.A.1.a.ix": {"title": "Other", "alternative_codes": ["5 A 1 a ix", "5A1aix"]},
        "5.A.1.b": {
            "title": "Other Forests",
            "alternative_codes": ["5 A 1 b", "5A1b"],
            "children": [["5.A.1.b.i", "5.A.1.b.ii", "5.A.1.b.iii"]],
        },
        "5.A.1.b.i": {"title": "Moist", "alternative_codes": ["5 A 1 b i", "5A1bi"]},
        "5.A.1.b.ii": {
            "title": "Seasonal",
            "alternative_codes": ["5 A 1 b ii", "5A1bii"],
        },
        "5.A.1.b.iii": {
            "title": "Dry",
            "alternative_codes": ["5 A 1 b iii", "5A1biii"],
        },
        "5.A.1.c": {"title": "Other", "alternative_codes": ["5 A 1 c", "5A1c"]},
        "5.A.2": {
            "title": "Temperate",
            "alternative_codes": ["5 A 2", "5A2"],
            "children": [["5.A.2.a", "5.A.2.b", "5.A.2.c"]],
        },
        "5.A.2.a": {"title": "Plantations", "alternative_codes": ["5 A 2 a", "5A2a"]},
        "5.A.2.b": {
            "title": "Commercial",
            "alternative_codes": ["5 A 2 b", "5A2b"],
            "children": [["5.A.2.b.i", "5.A.2.b.ii"]],
        },
        "5.A.2.b.i": {
            "title": "Evergreen",
            "alternative_codes": ["5 A 2 b i", "5A2bi"],
        },
        "5.A.2.b.ii": {
            "title": "Deciduous",
            "alternative_codes": ["5 A 2 b ii", "5A2bii"],
        },
        "5.A.2.c": {"title": "Other", "alternative_codes": ["5 A 2 c", "5A2c"]},
        "5.A.3": {"title": "Boreal", "alternative_codes": ["5 A 3", "5A3"]},
        "5.A.4": {
            "title": "Grasslands / Tundra",
            "alternative_codes": ["5 A 4", "5A4"],
        },
        "5.A.5": {
            "title": "Other",
            "alternative_codes": ["5 A 5", "5A5"],
            "children": [["5.A.5.a", "5.A.5.b"]],
        },
        "5.A.5.a": {
            "title": "Harvested Wood",
            "alternative_codes": ["5 A 5 a", "5A5a"],
        },
        "5.A.5.b": {"title": "Other", "alternative_codes": ["5 A 5 b", "5A5b"]},
        "5.D.1": {
            "title": "Cultivation of Mineral Soils",
            "alternative_codes": ["5 D 1", "5D1"],
            "children": [
                ["5.D.1.a", "5.D.1.b", "5.D.1.c", "5.D.1.d", "5.D.1.e", "5.D.1.f"]
            ],
        },
        "5.D.2": {
            "title": "Cultivation of Organic Soils",
            "alternative_codes": ["5 D 2", "5D2"],
            "children": [["5.D.2.a", "5.D.2.b", "5.D.2.c"]],
        },
        "5.D.3": {
            "title": "Liming of Agricultural Soils",
            "alternative_codes": ["5 D 3", "5D3"],
            "children": [["5.D.3.a", "5.D.3.b"]],
        },
        "5.D.4": {"title": "Forest Soils", "alternative_codes": ["5 D 4", "5D4"]},
        "5.D.5": {"title": "Other", "alternative_codes": ["5 D 5", "5D5"]},
        "5.B-tro": {
            "title": "Tropical Savanna / Grasslands",
            "alternative_codes": ["5 B-tro", "5B-tro"],
        },
        "5.B-gra": {"title": "Grasslands", "alternative_codes": ["5 B-gra", "5B-gra"]},
        "5.B.2-mix": {
            "title": "Mixed Broadleaf / Coniferous",
            "alternative_codes": ["5 B 2-mix", "5B2-mix"],
        },
        "5.C-tro": {
            "title": "Tropical Savanna / Grasslands",
            "alternative_codes": ["5 C-tro", "5C-tro"],
        },
        "5.C-gra": {"title": "Grasslands", "alternative_codes": ["5 C-gra", "5C-gra"]},
        "5.C.1.a": {
            "title": "Wet / Very Moist",
            "alternative_codes": ["5 C 1 a", "5C1a"],
        },
        "5.C.1.b": {
            "title": "Moist, short dry season",
            "alternative_codes": ["5 C 1 b", "5C1b"],
        },
        "5.C.1.c": {
            "title": "Moist, long dry season",
            "alternative_codes": ["5 C 1 c", "5C1c"],
        },
        "5.C.1.d": {"title": "Dry", "alternative_codes": ["5 C 1 d", "5C1d"]},
        "5.C.1.e": {"title": "Montane Moist", "alternative_codes": ["5 C 1 e", "5C1e"]},
        "5.C.1.f": {"title": "Montane Dry", "alternative_codes": ["5 C 1 f", "5C1f"]},
        "5.C.2.a": {
            "title": "Mixed Broadleaf / Coniferous",
            "alternative_codes": ["5 C 2 a", "5C2a"],
        },
        "5.C.2.b": {"title": "Coniferous", "alternative_codes": ["5 C 2 b", "5C2b"]},
        "5.C.2.c": {"title": "Broadleaf", "alternative_codes": ["5 C 2 c", "5C2c"]},
        "5.C.3.a": {
            "title": "Mixed Broadleaf / Coniferous",
            "alternative_codes": ["5 C 3 a", "5C3a"],
        },
        "5.C.3.b": {"title": "Coniferous", "alternative_codes": ["5 C 3 b", "5C3b"]},
        "5.C.3.c": {"title": "Broadleaf", "alternative_codes": ["5 C 3 c", "5C3c"]},
        "5.D.1.a": {
            "title": "High Activity Soils",
            "alternative_codes": ["5 D 1 a", "5D1a"],
        },
        "5.D.1.b": {
            "title": "Low Activity Soils",
            "alternative_codes": ["5 D 1 b", "5D1b"],
        },
        "5.D.1.c": {"title": "Sandy", "alternative_codes": ["5 D 1 c", "5D1c"]},
        "5.D.1.d": {"title": "Volcanic", "alternative_codes": ["5 D 1 d", "5D1d"]},
        "5.D.1.e": {
            "title": "Wetland (Aquic)",
            "alternative_codes": ["5 D 1 e", "5D1e"],
        },
        "5.D.1.f": {"title": "Other", "alternative_codes": ["5 D 1 f", "5D1f"]},
        "5.D.2.a": {
            "title": "Cool Temperate",
            "alternative_codes": ["5 D 2 a", "5D2a"],
            "children": [["5.D.2.a.i", "5.D.2.a.ii"]],
        },
        "5.D.2.a.i": {
            "title": "Upland Crops",
            "alternative_codes": ["5 D 2 a i", "5D2ai"],
        },
        "5.D.2.a.ii": {
            "title": "Pasture/Forest",
            "alternative_codes": ["5 D 2 a ii", "5D2aii"],
        },
        "5.D.2.b": {
            "title": "Warm Temperate",
            "alternative_codes": ["5 D 2 b", "5D2b"],
            "children": [["5.D.2.b.i", "5.D.2.b.ii"]],
        },
        "5.D.2.b.i": {
            "title": "Upland Crops",
            "alternative_codes": ["5 D 2 b i", "5D2bi"],
        },
        "5.D.2.b.ii": {
            "title": "Pasture/Forest",
            "alternative_codes": ["5 D 2 b ii", "5D2bii"],
        },
        "5.D.2.c": {
            "title": "Tropical",
            "alternative_codes": ["5 D 2 c", "5D2c"],
            "children": [["5.D.2.c.i", "5.D.2.c.ii"]],
        },
        "5.D.2.c.i": {
            "title": "Upland Crops",
            "alternative_codes": ["5 D 2 c i", "5D2ci"],
        },
        "5.D.2.c.ii": {
            "title": "Pasture/Forest",
            "alternative_codes": ["5 D 2 c ii", "5D2cii"],
        },
        "5.D.3.a": {"title": "Limestone", "alternative_codes": ["5 D 3 a", "5D3a"]},
        "5.D.3.b": {"title": "Dolomite", "alternative_codes": ["5 D 3 b", "5D3b"]},
        "6.A.2.a": {"title": "deep (>5 m)", "alternative_codes": ["6 A 2 a", "6A2a"]},
        "6.A.2.b": {
            "title": "shallow (<5 m)",
            "alternative_codes": ["6 A 2 b", "6A2b"],
        },
        "6.C.1": {"title": "biogenic", "alternative_codes": ["6 C 1", "6C1"]},
        "6.C.2": {"title": "plastics", "alternative_codes": ["6 C 2", "6C2"]},
        "6.C.3": {"title": "other", "alternative_codes": ["6 C 3", "6C3"]},
        "M.Memo": {
            "title": "Memo Items",
            "alternative_codes": ["M Memo", "MMemo"],
            "children": [["M.Memo.Bio", "M.Memo.Int", "M.Memo.Mult"]],
        },
        "M.Memo.Int": {
            "title": "International Bunkers",
            "alternative_codes": ["M Memo Int", "MMemoInt"],
            "children": [["M.Memo.Int.Avi", "M.Memo.Int.Mar"]],
        },
        "M.Memo.Int.Avi": {
            "title": "Aviation",
            "alternative_codes": ["M Memo Int Avi", "MMemoIntAvi"],
        },
        "M.Memo.Int.Mar": {
            "title": "Marine",
            "alternative_codes": ["M Memo Int Mar", "MMemoIntMar"],
        },
        "M.Memo.Mult": {
            "title": "Multilateral Operations",
            "alternative_codes": ["M Memo Mult", "MMemoMult"],
        },
        "M.Memo.Bio": {
            "title": "CO2 Emissions from Biomass",
            "alternative_codes": ["M Memo Bio", "MMemoBio"],
        },
    },
}
