spec = {
    "name": "IPCC2006_PRIMAP",
    "title": "IPCC GHG emission categories (2006) with custom categories used in PRIMAP",
    "comment": "IPCC classification of green-house gas emissions into categories, 2006 edition with additional categories needed for analyses and for datasets like PRIMAP-crf or EDGAR v6.0",
    "references": "",
    "institution": "PIK",
    "hierarchical": True,
    "last_update": "2021-10-12",
    "version": "2006",
    "total_sum": True,
    "canonical_top_level_category": "0",
    "categories": {
        "0": {
            "title": "National Total",
            "comment": "All emissions and removals",
            "children": [["1", "2", "3", "4", "5"], ["M.0.EL", "M.LULUCF"]],
        },
        "1": {
            "title": "Energy",
            "comment": "This category includes all GHG emissions arising from combustion and fugitive releases of fuels. Emissions from the non-energy uses of fuels are generally not included here, but reported under Industrial Processes and Product Use Sector.",
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
            "children": [["1.A", "1.B", "1.C"]],
        },
        "1.A": {
            "title": "Fuel Combustion Activities",
            "comment": "Emissions from the intentional oxidation of materials within an apparatus that is designed to raise heat and provide it either as heat or as mechanical work to a process or for use away from the apparatus.",
            "alternative_codes": ["1A"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A"],
            },
            "children": [["1.A.1", "1.A.2", "1.A.3", "1.A.4", "1.A.5"]],
        },
        "1.A.1": {
            "title": "Energy Industries",
            "comment": "Comprises  emissions  from  fuels  combusted  by  the  fuel extraction or energy-producing industries.",
            "alternative_codes": ["1A1"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A1"],
            },
            "children": [["1.A.1.a", "1.A.1.b", "1.A.1.c"], ["1.A.1.a", "1.A.1.bc"]],
        },
        "1.A.1.a": {
            "title": "Main Activity Electricity and Heat Production",
            "comment": "Sum of emissions from main activity producers of electricity generation, combined heat and power generation, and heat plants. Main activity producers (formerly known as public utilities) are defined as those undertakings whose primary activity is to supply the public. They may be in public or private ownership. Emissions from own on-site use of fuel should be included. Emissions from autoproducers (undertakings which generate electricity/heat wholly or partly for their own use, as an activity that supports their primary activity) should be assigned to the sector where they were generated and not under 1 A 1 a. Autoproducers may be in public or private ownership.",
            "alternative_codes": ["1A1a"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
            "children": [["1.A.1.a.i", "1.A.1.a.ii", "1.A.1.a.iii"]],
        },
        "1.A.1.a.i": {
            "title": "Electricity Generation",
            "comment": "Comprises emissions from all fuel use for electricity generation from main activity producers except those from combined heat and power plants.",
            "alternative_codes": ["1A1ai"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A1ai"],
            },
        },
        "1.A.1.a.ii": {
            "title": "Combined Heat and Power Generation (CHP)",
            "comment": "Emissions from production of both heat and electrical power from main activity producers for sale to the public, at a single CHP facility.",
            "alternative_codes": ["1A1aii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A1aii"],
            },
        },
        "1.A.1.a.iii": {
            "title": "Heat Plants",
            "comment": "Production of heat from main activity producers for sale by pipe network.",
            "alternative_codes": ["1A1aiii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A1aiii"],
            },
        },
        "1.A.1.b": {
            "title": "Petroleum Refining",
            "comment": "All combustion activities supporting the refining of petroleum products including on-site combustion for the generation of electricity and heat for own use. Does not include evaporative emissions occurring at the refinery. These emissions should be reported separately under 1 B 2 a.",
            "alternative_codes": ["1A1b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A1b"],
            },
        },
        "1.A.1.c": {
            "title": "Manufacture of Solid Fuels and Other Energy Industries",
            "comment": "Combustion emissions from fuel use during the manufacture of secondary and tertiary products from solid fuels including production of charcoal. Emissions from own on-site fuel use should be included. Also includes combustion for the generation of electricity and heat for own use in these industries.",
            "alternative_codes": ["1A1c"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A1c"],
            },
            "children": [["1.A.1.c.i", "1.A.1.c.ii"]],
        },
        "1.A.1.c.i": {
            "title": "Manufacture of Solid Fuels",
            "comment": "Emissions arising from fuel combustion for the production of coke, brown coal briquettes and patent fuel.",
            "alternative_codes": ["1A1ci"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A1ci"],
            },
        },
        "1.A.1.c.ii": {
            "title": "Other Energy Industries",
            "comment": "Combustion emissions arising from the energy-producing industries own (on-site) energy use not mentioned above or for which separate data are not available. This includes the emissions from own-energy use for the production of charcoal, bagasse, saw dust, cotton stalks and carbonizing of biofuels as well as fuel used for coal mining, oil and gas extraction and the processing and upgrading of natural gas. This category also includes emissions from pre-combustion processing for CO2 capture and storage. Combustion emissions from pipeline transport should be reported under 1 A 3 e.",
            "alternative_codes": ["1A1cii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A1cii"],
            },
        },
        "1.A.2": {
            "title": "Manufacturing Industries and Construction",
            "comment": "Emissions from combustion of fuels in industry. Also includes combustion for the generation of electricity and heat for own use in these industries. Emissions from fuel combustion in coke ovens within the iron and steel industry should be reported under 1 A 1 c and not within manufacturing industry. Emissions from the industry sector should be specified by sub-categories that correspond to the International Standard Industrial Classification of all Economic Activities (ISIC). Energy used for transport by industry should not be reported here but under Transport (1 A 3). Emissions arising from off-road and other mobile machinery in industry should, if possible, be broken out as a separate subcategory. For each country, the emissions from the largest fuel-consuming industrial categories ISIC should be reported, as well as those from significant emitters of pollutants. A suggested list of categories is outlined below.",
            "alternative_codes": ["1A2"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A2"],
            },
            "children": [
                [
                    "1.A.2.a",
                    "1.A.2.b",
                    "1.A.2.c",
                    "1.A.2.d",
                    "1.A.2.e",
                    "1.A.2.f",
                    "1.A.2.g",
                    "1.A.2.h",
                    "1.A.2.i",
                    "1.A.2.j",
                    "1.A.2.k",
                    "1.A.2.l",
                    "1.A.2.m",
                ],
                [
                    "1.A.2.a",
                    "1.A.2.b",
                    "1.A.2.c",
                    "1.A.2.d",
                    "1.A.2.e",
                    "1.A.2.f",
                    "M.1.A.2.m",
                ],
            ],
        },
        "1.A.2.a": {
            "title": "Iron and Steel",
            "comment": "ISIC Group 271 and Class 2731.",
            "alternative_codes": ["1A2a"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.A.2.b": {
            "title": "Non-Ferrous Metals",
            "comment": "ISIC Group 272 and Class 2732.",
            "alternative_codes": ["1A2b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A2b"],
            },
        },
        "1.A.2.c": {
            "title": "Chemicals",
            "comment": "ISIC Division 24.",
            "alternative_codes": ["1A2c"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A2c"],
            },
        },
        "1.A.2.d": {
            "title": "Pulp, Paper and Print",
            "comment": "ISIC Divisions 21 and 22.",
            "alternative_codes": ["1A2d"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A2d"],
            },
        },
        "1.A.2.e": {
            "title": "Food Processing, Beverages and Tobacco",
            "comment": "ISIC Divisions 15 and 16.",
            "alternative_codes": ["1A2e"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A2e"],
            },
        },
        "1.A.2.f": {
            "title": "Non-Metallic Minerals",
            "comment": "Includes products such as glass ceramic, cement, etc. ISIC Division 26.",
            "alternative_codes": ["1A2f"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A2f"],
            },
        },
        "1.A.2.g": {
            "title": "Transport Equipment",
            "comment": "ISIC Divisions 34 and 35.",
            "alternative_codes": ["1A2g"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.A.2.h": {
            "title": "Machinery",
            "comment": "Includes fabricated metal products, machinery and equipment other than transport equipment. ISIC Divisions 28, 29, 30, 31 and 32.",
            "alternative_codes": ["1A2h"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A2f"],
            },
        },
        "1.A.2.i": {
            "title": "Mining (Excluding Fuels) and Quarrying",
            "comment": "ISIC Divisions 13 and 14.",
            "alternative_codes": ["1A2i"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.A.2.j": {
            "title": "Wood and Wood Products",
            "comment": "ISIC Division 20.",
            "alternative_codes": ["1A2j"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.A.2.k": {
            "title": "Construction",
            "comment": "ISIC Division 45.",
            "alternative_codes": ["1A2k"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A2f"],
            },
        },
        "1.A.2.l": {
            "title": "Textile and Leather",
            "comment": "ISIC Divisions 17, 18 and 19.",
            "alternative_codes": ["1A2l"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.A.2.m": {
            "title": "Non-Specified Industry",
            "comment": "Any manufacturing industry/construction not included above or for which separate data are not available. Includes ISIC Divisions 25, 33, 36 and 37.",
            "alternative_codes": ["1A2m"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.A.3": {
            "title": "Transport",
            "comment": "Emissions from the combustion and evaporation of fuel for all transport activity (excluding military transport), regardless of the sector, specified by sub-categories below. Emissions from fuel sold to any air or marine vessel engaged in international transport (1 A 3 a i and 1 A 3 d i) should as far as possible be excluded from the totals and subtotals in this category and should be reported separately.",
            "alternative_codes": ["1A3"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3"],
            },
            "children": [
                ["1.A.3.a", "1.A.3.b", "1.A.3.c", "1.A.3.d", "1.A.3.e"],
                ["1.A.3.a", "1.A.3.b_noRES", "1.A.3.c", "1.A.3.d", "1.A.3.e"],
            ],
        },
        "1.A.3.a": {
            "title": "Civil Aviation",
            "comment": "Emissions from international and domestic civil aviation, including take-offs and landings.  Comprises civil commercial use of airplanes, including: scheduled and charter traffic for passengers and freight, air taxiing, and general aviation.  The international/domestic split should be determined on the basis of departure and landing locations for each flight stage and not by the nationality of the airline. Exclude use of fuel at airports for ground transport which is reported under 1 A 3 e Other Transportation. Also exclude fuel for stationary combustion at airports; report this information under the appropriate stationary combustion category.",
            "alternative_codes": ["1A3a"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3a"],
            },
            "children": [["1.A.3.a.i", "1.A.3.a.ii"]],
        },
        "1.A.3.a.i": {
            "title": "International Aviation (International Bunkers)",
            "comment": "Emissions from flights that depart in one country and arrive in a different country. Include take-offs and landings for these flight stages. Emissions from international military aviation can be included as a separate sub-category of international aviation provided that the same definitional distinction is applied and data are available to support the definition.",
            "alternative_codes": ["1A3ai"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3ai"],
            },
        },
        "1.A.3.a.ii": {
            "title": "Domestic Aviation",
            "comment": "Emissions from civil domestic passenger and freight traffic that departs and arrives in the same country (commercial, private, agriculture, etc.), including take-offs and landings for these flight stages.  Note that this may include journeys of considerable length between two airports in a country (e.g. San Francisco to Honolulu).  Exclude military, which should be reported under 1 A 5 b.",
            "alternative_codes": ["1A3aii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3aii"],
            },
        },
        "1.A.3.b": {
            "title": "Road Transportation",
            "comment": "All combustion and evaporative emissions arising from fuel use in road vehicles, including the use of agricultural vehicles on paved roads.",
            "alternative_codes": ["1A3b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3b"],
            },
            "children": [
                [
                    "1.A.3.b.i",
                    "1.A.3.b.ii",
                    "1.A.3.b.iii",
                    "1.A.3.b.iv",
                    "1.A.3.b.v",
                    "1.A.3.b.vi",
                ]
            ],
        },
        "1.A.3.b.i": {
            "title": "Cars",
            "comment": "Emissions from automobiles so designated in the vehicle registering country primarily for transport of persons and normally having a capacity of 12 persons or fewer.",
            "alternative_codes": ["1A3bi"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3bi"],
            },
            "children": [["1.A.3.b.i.1", "1.A.3.b.i.2"]],
        },
        "1.A.3.b.i.1": {
            "title": "Passenger Cars with 3-Way Catalysts",
            "comment": "Emissions from passenger car vehicles with 3-way catalysts.",
            "alternative_codes": ["1A3bi1"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3bi"],
            },
        },
        "1.A.3.b.i.2": {
            "title": "Passenger Cars without 3-Way Catalysts",
            "comment": "Passenger car emissions from vehicles without 3-way catalysts.",
            "alternative_codes": ["1A3bi2"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3bi"],
            },
        },
        "1.A.3.b.ii": {
            "title": "Light-Duty Trucks",
            "comment": "Emissions from vehicles so designated in the vehicle registering country primarily for transportation of light- weight cargo or which are equipped with special features such as four-wheel drive for off-road operation. The gross vehicle weight normally ranges up to 3500-3900 kg or less.",
            "alternative_codes": ["1A3bii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3bii", "1A3bi"],
            },
            "children": [["1.A.3.b.ii.1", "1.A.3.b.ii.2"]],
        },
        "1.A.3.b.ii.1": {
            "title": "Light-Duty Trucks with 3-Way Catalysts",
            "comment": "Emissions from light duty trucks with 3-way catalysts.",
            "alternative_codes": ["1A3bii1"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3bii"],
            },
        },
        "1.A.3.b.ii.2": {
            "title": "Light-Duty Trucks without 3-Way Catalysts",
            "comment": "Emissions from light duty trucks without 3-way catalysts.",
            "alternative_codes": ["1A3bii2"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3bii"],
            },
        },
        "1.A.3.b.iii": {
            "title": "Heavy-Duty Trucks and Buses",
            "comment": "Emissions from any vehicles so designated in the vehicle registering country. Normally the gross vehicle weight ranges from 3500-3900 kg or more for heavy duty trucks and the buses are rated to carry more than 12 persons.",
            "alternative_codes": ["1A3biii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3biii"],
            },
        },
        "1.A.3.b.iv": {
            "title": "Motorcycles",
            "comment": "Emissions from any motor vehicle designed to travel with not more than three wheels in contact with the ground and weighing less than 680 kg.",
            "alternative_codes": ["1A3biv"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3biv"],
            },
        },
        "1.A.3.b.v": {
            "title": "Evaporative Emissions from Vehicles",
            "comment": "Evaporative emissions from vehicles (e.g. hot soak, running losses) are included here. Emissions from loading fuel into vehicles are excluded.",
            "alternative_codes": ["1A3bv"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3bv"],
            },
        },
        "1.A.3.b.vi": {
            "title": "Urea-Based Catalysts",
            "comment": "CO2 emissions from use of urea-based additives in catalytic converters (non-combustive emissions).",
            "alternative_codes": ["1A3bvi"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.A.3.c": {
            "title": "Railways",
            "comment": "Emissions from railway transport for both freight and passenger traffic routes.",
            "alternative_codes": ["1A3c"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3c"],
            },
        },
        "1.A.3.d": {
            "title": "Water-Borne Navigation",
            "comment": "Emissions from fuels used to propel water-borne vessels, including hovercraft and hydrofoils, but excluding fishing vessels. The international/domestic split should be determined on the basis of port of departure and port of arrival, and not by the flag or nationality of the ship.",
            "alternative_codes": ["1A3d"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3d"],
            },
            "children": [["1.A.3.d.i", "1.A.3.d.ii"]],
        },
        "1.A.3.d.i": {
            "title": "International Water-Borne Navigation (International Bunkers)",
            "comment": "Emissions from fuels used by vessels of all flags that are engaged in international water-borne navigation. The international navigation may take place at sea, on inland lakes and waterways and in coastal waters.  Includes emissions from journeys that depart in one country and arrive in a different country. Exclude consumption by fishing vessels (see Other Sector - Fishing). Emissions from international military water-borne navigation can be included as a separate sub-category of international water- borne navigation provided that the same definitional distinction is applied and data are available to support the definition.",
            "alternative_codes": ["1A3di"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3di"],
            },
        },
        "1.A.3.d.ii": {
            "title": "Domestic Water-Borne Navigation",
            "comment": "Emissions from fuels used by vessels of all flags that depart and arrive in the same country (exclude fishing, which should be reported under 1 A 4 c iii, and military, which should be reported under 1 A 5 b). Note that this may include journeys of considerable length between two ports in a country (e.g. San Francisco to Honolulu).",
            "alternative_codes": ["1A3dii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3dii"],
            },
        },
        "1.A.3.e": {
            "title": "Other Transportation",
            "comment": "Combustion emissions from all remaining transport activities including pipeline transportation, ground activities in airports and harbours, and off-road activities not otherwise reported under 1 A 4 c Agriculture or 1 A 2. Manufacturing Industries and Construction. Military transport should be reported under 1 A 5 (see 1 A 5 Non- specified).",
            "alternative_codes": ["1A3e"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3e"],
            },
            "children": [["1.A.3.e.i", "1.A.3.e.ii"]],
        },
        "1.A.3.e.i": {
            "title": "Pipeline Transport",
            "comment": "Combustion related emissions from the operation of pump stations and maintenance of pipelines. Transport via pipelines includes transport of gases, liquids, slurry and other commodities via pipelines. Distribution of natural or manufactured gas, water or steam from the distributor to final users is excluded and should be reported in 1 A 1 c ii or 1 A 4 a.",
            "alternative_codes": ["1A3ei"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3e"],
            },
        },
        "1.A.3.e.ii": {
            "title": "Off-Road",
            "comment": "Combustion emissions from Other Transportation excluding Pipeline Transport.",
            "alternative_codes": ["1A3eii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A3e"],
            },
        },
        "1.A.4": {
            "title": "Other Sectors",
            "comment": "Emissions from combustion activities as described below, including combustion for the generation of electricity and heat for own use in these sectors.",
            "alternative_codes": ["1A4"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A4"],
            },
            "children": [["1.A.4.a", "1.A.4.b", "1.A.4.c"]],
        },
        "1.A.4.a": {
            "title": "Commercial/Institutional",
            "comment": "Emissions from fuel combustion in commercial and institutional buildings; all activities included in ISIC Divisions 41,50, 51, 52, 55, 63-67, 70-75, 80, 85, 90-93 and 99.",
            "alternative_codes": ["1A4a"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A4a"],
            },
        },
        "1.A.4.b": {
            "title": "Residential",
            "comment": "All emissions from fuel combustion in households.",
            "alternative_codes": ["1A4b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A4b"],
            },
        },
        "1.A.4.c": {
            "title": "Agriculture/Forestry/Fishing/Fish Farms",
            "comment": "Emissions from fuel combustion in agriculture, forestry, fishing and fishing industries such as fish farms. Activities included in ISIC Divisions 01, 02 and 05. Highway agricultural transportation is excluded.",
            "alternative_codes": ["1A4c"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A4c"],
            },
            "children": [["1.A.4.c.i", "1.A.4.c.ii", "1.A.4.c.iii"]],
        },
        "1.A.4.c.i": {
            "title": "Stationary",
            "comment": "Emissions from fuels combusted in pumps, grain drying, horticultural greenhouses and other agriculture, forestry or stationary combustion in the fishing industry.",
            "alternative_codes": ["1A4ci"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A4ci"],
            },
        },
        "1.A.4.c.ii": {
            "title": "Off-Road Vehicles and Other Machinery",
            "comment": "Emissions from fuels combusted in traction vehicles on farm land and in forests.",
            "alternative_codes": ["1A4cii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A4cii"],
            },
        },
        "1.A.4.c.iii": {
            "title": "Fishing (Mobile Combustion)",
            "comment": "Emissions from fuels combusted for inland, coastal and deep-sea fishing. Fishing should cover vessels of all flags that have refuelled in the country (include international fishing).",
            "alternative_codes": ["1A4ciii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A4ciii"],
            },
        },
        "1.A.5": {
            "title": "Non-Specified",
            "comment": "All remaining emissions from fuel combustion that are not specified elsewhere. Include emissions from fuel delivered to the military in the country and delivered to the military of other countries that are not engaged in multilateral operations Emissions from fuel sold to any air or marine vessel engaged in multilateral operation pursuant to the Charter of the United Nations should be excluded from the totals and subtotals of the military transport, and should be reported separately.",
            "alternative_codes": ["1A5"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A5"],
            },
            "children": [["1.A.5.a", "1.A.5.b", "1.A.5.c"]],
        },
        "1.A.5.a": {
            "title": "Stationary",
            "comment": "Emissions from fuel combustion in stationary sources that are not specified elsewhere.",
            "alternative_codes": ["1A5a"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A5a"],
            },
        },
        "1.A.5.b": {
            "title": "Mobile",
            "comment": "Emissions from vehicles and other machinery, marine and aviation (not included in 1 A 4 c ii or elsewhere).",
            "alternative_codes": ["1A5b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1A5b"],
            },
            "children": [["1.A.5.b.i", "1.A.5.b.ii", "1.A.5.b.iii"]],
        },
        "1.A.5.b.i": {
            "title": "Mobile (Aviation Component)",
            "comment": "All remaining aviation emissions from fuel combustion that are not specified elsewhere. Include emissions from fuel delivered to the country’s military not otherwise included separately in 1 A3 a i as well as fuel delivered within that country but used by militaries of other countries that are not engaged in multilateral operation pursuant to the Charter of the United Nations.",
            "alternative_codes": ["1A5bi"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.A.5.b.ii": {
            "title": "Mobile (Water-Borne Component)",
            "comment": "All remaining water-borne emissions from fuel combustion that are not specified elsewhere. Include emissions from fuel delivered to the country’s military not otherwise included separately in 1 A3 d i as well as fuel delivered within that country but used by militaries of other countries that are not engaged in multilateral operation pursuant to the Charter of the United Nations.",
            "alternative_codes": ["1A5bii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.A.5.b.iii": {
            "title": "Mobile (Other)",
            "comment": "All remaining emissions from mobile sources not included elsewhere.",
            "alternative_codes": ["1A5biii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.A.5.c": {
            "title": "Multilateral Operations",
            "comment": "Emissions from fuel sold to any air or marine vessel engaged in multilateral operations pursuant to the Charter of the United Nations should be excluded from the totals and subtotals of the military transport, and should be reported separately.",
            "alternative_codes": ["1A5c"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "1.B": {
            "title": "Fugitive Emissions from Fuels",
            "comment": "Includes all intentional and unintentional emissions from the extraction, processing, storage and transport of fuel to the point of final use.",
            "alternative_codes": ["1B"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B"],
            },
            "children": [["1.B.1", "1.B.2", "1.B.3"]],
        },
        "1.B.1": {
            "title": "Solid Fuels",
            "comment": "Includes all intentional and unintentional emissions from the extraction, processing, storage and transport of fuel to the point of final use.",
            "alternative_codes": ["1B1"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["1B1"],
            },
            "children": [["1.B.1.a", "1.B.1.b", "1.B.1.c"]],
        },
        "1.B.1.a": {
            "title": "Coal Mining and Handling",
            "comment": "Includes all fugitive emissions from coal.",
            "alternative_codes": ["1B1a"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["1B1a"],
            },
            "children": [["1.B.1.a.i", "1.B.1.a.ii"]],
        },
        "1.B.1.a.i": {
            "title": "Underground Mines",
            "comment": "Includes all emissions arising from mining, post-mining, abandoned mines and flaring of drained methane.",
            "alternative_codes": ["1B1ai"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["1B1ai"],
            },
            "children": [["1.B.1.a.i.1", "1.B.1.a.i.2", "1.B.1.a.i.3", "1.B.1.a.i.4"]],
        },
        "1.B.1.a.i.1": {
            "title": "Mining",
            "comment": "Includes all seam gas emissions vented to atmosphere from coal mine ventilation air and degasification systems.",
            "alternative_codes": ["1B1ai1"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["1B1ai"],
            },
        },
        "1.B.1.a.i.2": {
            "title": "Post-Mining Seam Gas Emissions",
            "comment": "Includes methane and CO2 emitted after coal has been mined, brought to the surface and subsequently processed, stored and transported.",
            "alternative_codes": ["1B1ai2"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["1B1ai"],
            },
        },
        "1.B.1.a.i.3": {
            "title": "Abandoned Underground Mines",
            "comment": "Includes methane emissions from abandoned underground mines.",
            "alternative_codes": ["1B1ai3"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["1B1ai"],
            },
        },
        "1.B.1.a.i.4": {
            "title": "Flaring of Drained Methane or Conversion of Methane to CO2",
            "comment": "Methane drained and flared, or ventilation gas converted to CO2 by an oxidation process should be included here. Methane used for energy production should be included in Volume 2, Energy, Chapter 2 ‘Stationary Combustion’.",
            "alternative_codes": ["1B1ai4"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["1B1ai"],
            },
        },
        "1.B.1.a.ii": {
            "title": "Surface Mines",
            "comment": "Includes all seam gas emissions arising from surface  coal mining.",
            "alternative_codes": ["1B1aii"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["1B1aii"],
            },
            "children": [["1.B.1.a.ii.1", "1.B.1.a.ii.2"]],
        },
        "1.B.1.a.ii.1": {
            "title": "Mining",
            "comment": "Includes methane and CO2 emitted during mining from breakage of coal and associated strata and leakage from the pit floor and high wall.",
            "alternative_codes": ["1B1aii1"],
            "info": {"gases": ["CO2", "CH4"]},
        },
        "1.B.1.a.ii.2": {
            "title": "Post-Mining Seam Gas Emissions",
            "comment": "Includes methane and CO2 emitted after coal has been mined, subsequently processed, stored and transported.",
            "alternative_codes": ["1B1aii2"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["1B1aii"],
            },
        },
        "1.B.1.b": {
            "title": "Uncontrolled Combustion, and Burning Coal Dumps",
            "comment": "Includes fugitive emissions of CO2 from uncontrolled combustion in coal.",
            "alternative_codes": ["1B1b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1B1c"],
            },
        },
        "1.B.1.c": {
            "title": "Solid Fuel Transformation",
            "comment": "Fugitive emissions arising during the manufacture of secondary and tertiary products from solid fuels.",
            "alternative_codes": ["1B1c"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1B1b"],
            },
        },
        "1.B.2": {
            "title": "Oil and Natural Gas",
            "comment": "Comprises fugitive emissions from all oil and natural gas activities. The primary sources of these emissions may include fugitive equipment leaks, evaporation losses, venting, flaring and accidental releases.",
            "alternative_codes": ["1B2"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2"],
            },
            "children": [["1.B.2.a", "1.B.2.b"]],
        },
        "1.B.2.a": {
            "title": "Oil",
            "comment": "Comprises emissions from venting, flaring and all other fugitive sources associated with the exploration, production, transmission, upgrading, and refining of crude oil and distribution of crude oil products.",
            "alternative_codes": ["1B2a"],
            "info": {
                "gases": ["CO2", "CH4", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2a"],
            },
            "children": [["1.B.2.a.i", "1.B.2.a.ii", "1.B.2.a.iii"]],
        },
        "1.B.2.a.i": {
            "title": "Venting",
            "comment": "Emissions from venting of associated gas and waste gas/vapour streams at oil facilities.",
            "alternative_codes": ["1B2ai"],
            "info": {"gases": ["CO2", "CH4", "NMVOC"]},
        },
        "1.B.2.a.ii": {
            "title": "Flaring",
            "comment": "Emissions from flaring of natural gas and waste gas/vapour streams at oil facilities.",
            "alternative_codes": ["1B2aii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"]},
        },
        "1.B.2.a.iii": {
            "title": "All Other",
            "comment": "Fugitive emissions at oil facilities from equipment leaks, storage losses, pipeline breaks, well blowouts, land farms, gas  migration to the surface around the outside of wellhead casing, surface casing vent bows, biogenic gas formation from tailings ponds and any other gas or vapour releases not specifically accounted for as venting or flaring.",
            "alternative_codes": ["1B2aiii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"]},
            "children": [
                [
                    "1.B.2.a.iii.1",
                    "1.B.2.a.iii.2",
                    "1.B.2.a.iii.3",
                    "1.B.2.a.iii.4",
                    "1.B.2.a.iii.5",
                    "1.B.2.a.iii.6",
                ]
            ],
        },
        "1.B.2.a.iii.1": {
            "title": "Exploration",
            "comment": "Fugitive emissions (excluding venting and flaring) from oil well drilling, drill stem testing, and well completions.",
            "alternative_codes": ["1B2aiii1"],
            "info": {
                "gases": ["CO2", "CH4", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2ai"],
            },
        },
        "1.B.2.a.iii.2": {
            "title": "Production and Upgrading",
            "comment": "Fugitive emissions from oil production (excluding venting and flaring) occur at the oil wellhead or at the oil sands or shale oil mine through to the start of the oil transmission system. This includes fugitive emissions related to well servicing, oil sands or shale oil mining, transport of untreated production (i.e , well effluent, emulsion, oil shale and oilsands) to  treating or extraction facilities, activities at extraction and upgrading facilities, associated gas re- injection systems and produced water disposal systems. Fugitive emission from upgraders are grouped with those from production rather than those from refining since the upgraders are often integrated with extraction facilities and their relative emission contributions are difficult to establish. However, upgraders may also be integrated with refineries, co-generation plants or other industrial facilities and their relative emission contributions can be difficult to establish in these cases.",
            "alternative_codes": ["1B2aiii2"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2aii"],
            },
        },
        "1.B.2.a.iii.3": {
            "title": "Transport",
            "comment": "Fugitive emissions (excluding venting and flaring) related to the transport of marketable crude oil (including conventional, heavy and synthetic crude oil and bitumen) to upgraders and refineries. The transportation systems may comprise pipelines, marine tankers, tank trucks and rail cars. Evaporation losses from storage, filling and unloading activities and fugitive equipment leaks are the primary sources of these emissions.",
            "alternative_codes": ["1B2aiii3"],
            "info": {
                "gases": ["CO2", "CH4", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2aiii"],
            },
        },
        "1.B.2.a.iii.4": {
            "title": "Refining",
            "comment": "Fugitive emissions (excluding venting and flaring) at petroleum refineries. Refineries process crude oils, natural gas liquids and synthetic crude oils to produce final refined products (e.g., primarily fuels and lubricants). Where refineries are integrated with other facilities (for example, upgraders or co-generation plants) their relative emission contributions can be difficult to establish.",
            "alternative_codes": ["1B2aiii4"],
            "info": {
                "gases": ["CO2", "CH4", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2aiv"],
            },
        },
        "1.B.2.a.iii.5": {
            "title": "Distribution of Oil Products",
            "comment": "This comprises fugitive emissions (excluding venting and flaring) from the transport and distribution of refined products, including those at bulk terminals and retail facilities. Evaporation losses from storage, filling and unloading activities and fugitive equipment leaks are the primary sources of these emissions.",
            "alternative_codes": ["1B2aiii5"],
            "info": {
                "gases": ["CO2", "CH4", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2av"],
            },
        },
        "1.B.2.a.iii.6": {
            "title": "Other",
            "comment": "Fugitive emissions from oil systems (excluding venting and flaring) not otherwise accounted for in the above categories. This includes fugitive emissions from spills and other accidental releases, waste oil treatment facilities and oilfield waste disposal facilities.",
            "alternative_codes": ["1B2aiii6"],
            "info": {
                "gases": ["CO2", "CH4", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2avi"],
            },
        },
        "1.B.2.b": {
            "title": "Natural Gas",
            "comment": "Comprises emissions from venting, flaring and all other fugitive sources associated with the exploration, production, processing, transmission, storage and distribution of natural gas (including both associated and non-associated gas).",
            "alternative_codes": ["1B2b"],
            "info": {
                "gases": ["CO2", "CH4", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2b"],
            },
            "children": [["1.B.2.b.i", "1.B.2.b.ii", "1.B.2.b.iii"]],
        },
        "1.B.2.b.i": {
            "title": "Venting",
            "comment": "Emissions from venting of natural gas and waste gas/vapour streams at gas facilities.",
            "alternative_codes": ["1B2bi"],
            "info": {"gases": ["CO2", "CH4", "NMVOC"]},
        },
        "1.B.2.b.ii": {
            "title": "Flaring",
            "comment": "Emissions from flaring of natural gas and waste gas/vapour streams at gas facilities.",
            "alternative_codes": ["1B2bii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"]},
        },
        "1.B.2.b.iii": {
            "title": "All Other",
            "comment": "Fugitive emissions at natural gas facilities from equipment leaks, storage losses, pipeline breaks, well blowouts, gas migration to the surface around the outside of wellhead casing, surface casing vent bows and any other gas or vapour releases not specifically accounted for as venting or flaring.",
            "alternative_codes": ["1B2biii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"]},
            "children": [
                [
                    "1.B.2.b.iii.1",
                    "1.B.2.b.iii.2",
                    "1.B.2.b.iii.3",
                    "1.B.2.b.iii.4",
                    "1.B.2.b.iii.5",
                    "1.B.2.b.iii.6",
                ]
            ],
        },
        "1.B.2.b.iii.1": {
            "title": "Exploration",
            "comment": "Fugitive emissions (excluding venting and flaring) from gas well drilling, drill stem testing and well completions.",
            "alternative_codes": ["1B2biii1"],
            "info": {"gases": ["CO2", "CH4", "NMVOC"]},
        },
        "1.B.2.b.iii.2": {
            "title": "Production",
            "comment": "Fugitive emissions (excluding venting and flaring) from the gas wellhead through to the inlet of gas processing plants, or, where processing is not required, to the tie-in points on gas transmission systems. This includes fugitive emissions related to well servicing, gas gathering, processing and associated waste water and acid gas disposal activities.",
            "alternative_codes": ["1B2biii2"],
            "info": {"gases": ["CO2", "CH4", "NMVOC"]},
        },
        "1.B.2.b.iii.3": {
            "title": "Processing",
            "comment": "Fugitive emissions (excluding venting and flaring) from gas processing facilities.",
            "alternative_codes": ["1B2biii3"],
            "info": {"gases": ["CO2", "CH4", "NMVOC"]},
        },
        "1.B.2.b.iii.4": {
            "title": "Transmission and Storage",
            "comment": "Fugitive emissions from systems used to transport processed natural gas to market (i.e., to industrial consumers and natural gas distribution systems). Fugitive emissions from natural gas storage systems should also be included in this category. Emissions from natural gas liquids extraction plants on gas transmission systems should be reported as part of natural gas processing (Sector 1.B.2.b.iii.3). Fugitive emissions related to the transmission of natural gas liquids should be reported under Category 1.B.2.a.iii.3.",
            "alternative_codes": ["1B2biii4"],
            "info": {
                "gases": ["CO2", "CH4", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2bii"],
            },
        },
        "1.B.2.b.iii.5": {
            "title": "Distribution",
            "comment": "Fugitive emissions (excluding venting and flaring) from the distribution of natural gas to end users.",
            "alternative_codes": ["1B2biii5"],
            "info": {"gases": ["CO2", "CH4", "NMVOC"]},
        },
        "1.B.2.b.iii.6": {
            "title": "Other",
            "comment": "Fugitive emissions from natural gas systems (excluding venting and flaring) not otherwise accounted for in the above categories. This may include emissions from well blowouts and pipeline ruptures or dig-ins.",
            "alternative_codes": ["1B2biii6"],
            "info": {
                "gases": ["CO2", "CH4", "NMVOC"],
                "corresponding_categories_IPCC1996": ["1B2c"],
            },
        },
        "1.B.3": {
            "title": "Other Emissions from Energy Production",
            "comment": "Other fugitive emissions for example, from geo thermal energy production, peat and other energy production not included in 1.B.2.",
            "alternative_codes": ["1B3"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"]},
        },
        "1.C": {
            "title": "Carbon Dioxide Transport and Storage",
            "comment": "Carbon dioxide (CO2) capture and storage (CCS) involves the capture of CO2 from anthropogenic sources, its transport to a storage location and its long-term isolation from the atmosphere.  Emissions associated with CO2 transport, injection and storage are covered under category 1C.  Emissions (and reductions) associated with CO2 capture should be reported under the IPCC Sector in which capture takes place (e.g. Fuel Combustion or Industrial Activities).",
            "alternative_codes": ["1C"],
            "info": {"gases": ["CO2"]},
            "children": [["1.C.1", "1.C.2", "1.C.3"]],
        },
        "1.C.1": {
            "title": "Transport of CO2",
            "comment": "This comprises fugitive emissions from the systems used to transport captured CO2 from the source to the injection site. These emissions may comprise losses due to fugitive equipment leaks, venting and releases due to pipeline ruptures or other accidental releases (e.g., temporary storage).",
            "alternative_codes": ["1C1"],
            "info": {"gases": ["CO2"]},
            "children": [["1.C.1.a", "1.C.1.b", "1.C.1.c"]],
        },
        "1.C.1.a": {
            "title": "Pipelines",
            "comment": "Fugitive emissions from the pipeline system used to transport CO2 to the injection site.",
            "alternative_codes": ["1C1a"],
            "info": {"gases": ["CO2"]},
        },
        "1.C.1.b": {
            "title": "Ships",
            "comment": "Fugitive emissions from the ships used to transport CO2 to the injection site.",
            "alternative_codes": ["1C1b"],
            "info": {"gases": ["CO2"]},
        },
        "1.C.1.c": {
            "title": "Other (Please Specify)",
            "comment": "Fugitive emissions from other systems used to transport CO2 to the injection site and temporary storage",
            "alternative_codes": ["1C1c"],
            "info": {"gases": ["CO2"]},
        },
        "1.C.2": {
            "title": "Injection and Storage",
            "comment": "Fugitive emissions from activities and equipment at the injection site and those from the end containment once the CO2 is placed in storage.",
            "alternative_codes": ["1C2"],
            "info": {"gases": ["CO2"]},
            "children": [["1.C.2.a", "1.C.2.b"]],
        },
        "1.C.2.a": {
            "title": "Injection",
            "comment": "Fugitive emissions from activities and equipment at the injection site.",
            "alternative_codes": ["1C2a"],
            "info": {"gases": ["CO2"]},
        },
        "1.C.2.b": {
            "title": "Storage",
            "comment": "Fugitive emissions from the end equipment once the CO2 is placed in storage.",
            "alternative_codes": ["1C2b"],
            "info": {"gases": ["CO2"]},
        },
        "1.C.3": {
            "title": "Other",
            "comment": "Any other emissions from CCS not reported elsewhere.",
            "alternative_codes": ["1C3"],
            "info": {"gases": ["CO2"]},
        },
        "2": {
            "title": "Industrial Processes and Product Use",
            "comment": "Emissions from industrial processes and product use, excluding those related to energy combustion (reported under 1A), extraction, processing and transport of fuels (reported under 1B) and CO2 transport, injection and storage (reported under 1C).",
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "HFCs",
                    "PFCs",
                    "SF6",
                    "other halogenated gases",
                    "NOx",
                    "CO",
                    "NMVOC",
                    "SO2",
                ]
            },
            "children": [["2.A", "2.B", "2.C", "2.D", "2.E", "2.F", "2.G", "2.H"]],
        },
        "2.A": {
            "title": "Mineral Industry",
            "alternative_codes": ["2A"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2A"],
            },
            "children": [["2.A.1", "2.A.2", "2.A.3", "2.A.4", "2.A.5"]],
        },
        "2.A.1": {
            "title": "Cement Production",
            "comment": "Process-related emissions from the production of various types of cement (ISIC: D2694).",
            "alternative_codes": ["2A1"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["2A1"],
            },
        },
        "2.A.2": {
            "title": "Lime Production",
            "comment": "Process-related emissions from the production of various types of lime (ISIC: D2694).",
            "alternative_codes": ["2A2"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["2A2"],
            },
        },
        "2.A.3": {
            "title": "Glass Production",
            "comment": "Process-related emissions from the production of various types of glass (ISIC: D2610).",
            "alternative_codes": ["2A3"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["2A3", "2A4"],
            },
        },
        "2.A.4": {
            "title": "Other Process Uses of Carbonates",
            "comment": "Includes limestone, dolomite and other carbonates etc. Emissions from the use of limestone, dolomite and other carbonates should be included in the industrial source category where they are emitted. Therefore, for example, where a carbonate is used as a flux for iron and steel production, resultant emissions should be reported under 2C1 “Iron and Steel Production” rather than this subcategory.",
            "alternative_codes": ["2A4"],
            "info": {
                "gases": ["CO2", "CH4", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2A3", "2A4"],
            },
            "children": [["2.A.4.a", "2.A.4.b", "2.A.4.c", "2.A.4.d"]],
        },
        "2.A.4.a": {
            "title": "Ceramics",
            "comment": "Process-related emissions from the production of bricks and roof tiles, vitrified clay pipes, refractory products, expanded clay products, wall and floor tiles, table and ornamental ware (household ceramics), sanitary ware, technical ceramics, and inorganic bonded abrasives (ISIC: D2691, D2692 and D2693).",
            "alternative_codes": ["2A4a"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["2A3"],
            },
        },
        "2.A.4.b": {
            "title": "Other Uses of Soda Ash",
            "comment": "This should include emissions from soda ash use that are not included elsewhere. For example, soda ash used for glass should be reported in 2A3.",
            "alternative_codes": ["2A4b"],
            "info": {
                "gases": ["CO2", "CH4", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2A4"],
            },
        },
        "2.A.4.c": {
            "title": "Non Metallurgical Magnesia Production",
            "comment": "This source category should include emissions from magnesia production that are not included elsewhere. For example, where magnesia production is used for primary and secondary magnesium production, emissions should be reported in relevant source category in Metals.",
            "alternative_codes": ["2A4c"],
            "info": {
                "gases": ["CO2", "CH4"],
                "corresponding_categories_IPCC1996": ["2A3"],
            },
        },
        "2.A.4.d": {
            "title": "Other (Please Specify)",
            "comment": "Process-related emissions reported under this sub-category should include all other miscellaneous uses of limestone, dolomite and other carbonates, except from uses already listed in the sub-categories above, and uses as fluxes or slagging agents in the Metals and Chemicals industries, or for the liming of soils and wetlands in Agriculture, Forestry and Other Land Uses (ISIC D269).",
            "alternative_codes": ["2A4d"],
            "info": {
                "gases": ["CO2", "CH4", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2A3"],
            },
        },
        "2.A.5": {
            "title": "Other (Please Specify)",
            "alternative_codes": ["2A5"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2A7"],
            },
        },
        "2.B": {
            "title": "Chemical Industry",
            "alternative_codes": ["2B"],
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "HFCs",
                    "PFCs",
                    "SF6",
                    "other halogenated gases",
                    "NOx",
                    "CO",
                    "NMVOC",
                    "SO2",
                ],
                "corresponding_categories_IPCC1996": ["2B", "2A4", "3C"],
            },
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
            "comment": "Ammonia (NH3) is a major industrial chemical and the most important nitrogenous material produced. Ammonia gas is used directly as a fertilizer, in heat treating, paper pulping, nitric acid and nitrates manufacture, nitric acid ester and nitro compound manufacture, explosives of various types, and as a refrigerant. Amines, amides, and miscellaneous other organic compounds, such as urea, are made from ammonia. The main greenhouse gas emitted from NH3 production is CO2. CO2 used in the production of urea, a downstream process, should be subtracted from the CO2 generated and accounted for in the AFOLU Sector.",
            "alternative_codes": ["2B1"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2B1"],
            },
        },
        "2.B.2": {
            "title": "Nitric Acid Production",
            "comment": "Nitric acid is used as a raw material mainly in the manufacture of nitrogenous-based fertiliser.  Nitric acid may also be used in the production of adipic acid and explosives (e.g., dynamite), for metal etching and in the processing of ferrous metals. The main greenhouse gas emitted from HNO3 production is nitrous oxide.",
            "alternative_codes": ["2B2"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["2B2"],
            },
        },
        "2.B.3": {
            "title": "Adipic Acid Production",
            "comment": "Adipic acid is used in the manufacture of a large number of products including synthetic fibres, coatings, plastics, urethane foams, elastomers and synthetic lubricants. The production of Nylon 6.6 accounts for the bulk of adipic acid use. The main greenhouse gas emitted from adipic acid production is nitrous oxide.",
            "alternative_codes": ["2B3"],
            "info": {
                "gases": ["N2O", "CO2", "CH4", "NOx"],
                "corresponding_categories_IPCC1996": ["2B3"],
            },
        },
        "2.B.4": {
            "title": "Caprolactam, Glyoxal and Glyoxylic Acid Production",
            "comment": "Most of the annual production of caprolactam (NH(CH2)5CO) is consumed as the monomer for nylon-6 fibres and plastics, with a substantial proportion of the fibre used in carpet manufacturing. All commercial processes for the manufacture of caprolactam are based on either toluene or benzene. This subcategory also covers production of glyoxal (ethanedial) and glyoxylic acid production. The main greenhouse gas emitted from this subcategory is nitrous oxide.",
            "alternative_codes": ["2B4"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["2B5"],
            },
        },
        "2.B.5": {
            "title": "Carbide Production",
            "comment": "The production of carbide can result in emissions of CO2, CH4, CO and SO2. Silicon carbide is a significant artificial abrasive. It is produced from silica sand or quartz and petroleum coke. Calcium carbide is used in the production of acetylene, in the manufacture of cyanamide (a minor historical use), and as a reductant in electric arc steel furnaces. It is made from calcium carbonate (limestone) and carbon-containing reductant (petroleum coke).",
            "alternative_codes": ["2B5"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["2B4"],
            },
        },
        "2.B.6": {
            "title": "Titanium Dioxide Production",
            "comment": "Titanium dioxide (TiO2) is the most important white pigment. The main use is in paint manufacture followed by paper, plastics, rubber, ceramics, fabrics, floor covering, printing ink, and other miscellaneous uses. The main production process is the chloride route, giving rise to CO2 emissions that are likely to be significant. This category also includes synthetic rutile production using the Becher process, and titanium slag production, both of which are reduction processes using fossil fuels and resulting in CO2 emissions. Synthetic rutile is the major input to TiO2 production using the chloride route.",
            "alternative_codes": ["2B6"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["2B5"],
            },
        },
        "2.B.7": {
            "title": "Soda Ash Production",
            "comment": "Soda ash (sodium carbonate, Na2CO3) is a white crystalline solid that is used as a raw material in a large number of industries including glass manufacture, soap and detergents, pulp and paper production and water treatment. Emissions of CO2 from the production of soda ash vary dependent on the manufacturing process. Four different processes may be used to produce soda ash. Three of these processes, monohydrate, sodium sesquicarbonate (trona) and direct carbonation, are referred to as natural processes. The fourth, the Solvay process, is classified as a synthetic process.",
            "alternative_codes": ["2B7"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["2A4"],
            },
        },
        "2.B.8": {
            "title": "Petrochemical and Carbon Black Production",
            "alternative_codes": ["2B8"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2B5"],
            },
            "children": [
                ["2.B.8.a", "2.B.8.b", "2.B.8.c", "2.B.8.d", "2.B.8.e", "2.B.8.f"]
            ],
        },
        "2.B.8.a": {
            "title": "Methanol",
            "comment": "Methanol production covers production of methanol from fossil fuel feedstocks [natural gas, petroleum, coal] using steam reforming or partial oxidation processes.  Production of methanol from biogenic feedstocks (e.g., by fermentation) is not included in this source category.",
            "alternative_codes": ["2B8a"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NMVOC"],
                "corresponding_categories_IPCC1996": ["2B5"],
            },
        },
        "2.B.8.b": {
            "title": "Ethylene",
            "comment": "Ethylene production covers production of ethylene from fossil fuel-derived feedstocks at petrochemical plants by the steam cracking process.  Production of ethylene from processes situation within the boundaries of petroleum refineries is not included in this source category.  The greenhouse gases produced from ethylene production are carbon dioxide and methane.",
            "alternative_codes": ["2B8b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2B5"],
            },
        },
        "2.B.8.c": {
            "title": "Ethylene Dichloride and Vinyl Chloride Monomer",
            "comment": "Ethylene dichloride and vinyl chloride monomer production covers production of ethylene dichloride by direct oxidation or oxychloination of ethylene, and the production of vinyl chloride monomer from ethylene dichloride.   The greenhouse gases produced from production of ethylene dichloride production and vinyl chloride monomer production are carbon dioxide and methane.",
            "alternative_codes": ["2B8c"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["2B5"],
            },
        },
        "2.B.8.d": {
            "title": "Ethylene Oxide",
            "comment": "Ethylene oxide production covers production of ethylene oxide by reaction of ethylene and oxygen by catalytic oxidation.   The greenhouse gases produced from ethylene oxide production are carbon dioxide and methane.",
            "alternative_codes": ["2B8d"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2B5"],
            },
        },
        "2.B.8.e": {
            "title": "Acrylonitrile",
            "comment": "Acrylonitrile production covers production of acrylonitrile from ammoxidation of propylene, and associated production of acetonitrile and hydrogen cyanide from the ammoxidation process.  The greenhouse gases produced from production of acrylonitrile are carbon dioxide and methane.",
            "alternative_codes": ["2B8e"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NMVOC"],
                "corresponding_categories_IPCC1996": ["2B5"],
            },
        },
        "2.B.8.f": {
            "title": "Carbon Black",
            "comment": "Carbon black production covers production of carbon black from fossil fuel-derived feedstocks (petroleum or coal- derived carbon black feedstock, natural gas, acetylene). Production of carbon black from biogenic feedstocks is not included in this source category.",
            "alternative_codes": ["2B8f"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2B5", "3C"],
            },
        },
        "2.B.9": {
            "title": "Fluorochemical Production",
            "alternative_codes": ["2B9"],
            "info": {
                "gases": ["HFCs", "PFCs", "SF6", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2E"],
            },
            "children": [["2.B.9.a", "2.B.9.b"]],
        },
        "2.B.9.a": {
            "title": "By-Product Emissions",
            "comment": "Fluorochemical Production covers the complete range of fluorochemicals, whether or not the principal products are greenhouse gases. Emissions encompass HFCs, PFCs, SF6 and all other halogenated gases with global warming potential listed in IPCC assessment reports. The most significant by-product emission is that of HFC-23 from the manufacture of HCFC-22 and this is described separately.",
            "alternative_codes": ["2B9a"],
            "info": {
                "gases": ["HFCs", "PFCs", "SF6", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2E1"],
            },
        },
        "2.B.9.b": {
            "title": "Fugitive Emissions",
            "comment": "These are emissions of the principal product from the process to manufacture it and so fluorochemical production in this context is limited to HFCs, PFCs, SF6 and other halogenated gases with global warming potential listed in IPCC assessment reports.",
            "alternative_codes": ["2B9b"],
            "info": {
                "gases": ["HFCs", "PFCs", "SF6", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2E2"],
            },
        },
        "2.B.10": {
            "title": "Other (Please Specify)",
            "comment": "For example, gases with global warming potential listed in IPCC assessment reports that do not fall within any categories above could be reported here, if they are estimated.",
            "alternative_codes": ["2B10"],
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "HFCs",
                    "PFCs",
                    "SF6",
                    "other halogenated gases",
                    "NOx",
                    "CO",
                    "NMVOC",
                    "SO2",
                ],
                "corresponding_categories_IPCC1996": ["2B5"],
            },
        },
        "2.C": {
            "title": "Metal Industry",
            "alternative_codes": ["2C"],
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "HFCs",
                    "PFCs",
                    "SF6",
                    "other halogenated gases",
                    "NOx",
                    "CO",
                    "NMVOC",
                    "SO2",
                ],
                "corresponding_categories_IPCC1996": ["2C"],
            },
            "children": [
                ["2.C.1", "2.C.2", "2.C.3", "2.C.4", "2.C.5", "2.C.6", "2.C.7"]
            ],
        },
        "2.C.1": {
            "title": "Iron and Steel Production",
            "comment": "Carbon dioxide is the predominant gas emitted from the production of iron and steel.  The sources of the carbon dioxide emissions include that from carbon-containing reducing agents such as coke and pulverized coal, and, from minerals such as limestone and dolomite added.",
            "alternative_codes": ["2C1"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2C1"],
            },
        },
        "2.C.2": {
            "title": "Ferroalloys Production",
            "comment": "Ferroalloys production covers emissions from primary metallurgical reduction production of the most common ferroalloys, i.e. ferro-silicon, silicon metal, ferro-manganese, silicon manganese, and ferro-chromium, excluding those emissions relating to fuel use. From the production of these alloys, carbon dioxide (CO2), nitrous oxide (N2O), and methane (CH4) originating from ore- and reductant raw materials, is emitted.",
            "alternative_codes": ["2C2"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2C2"],
            },
        },
        "2.C.3": {
            "title": "Aluminium Production",
            "comment": "Aluminium Production covers primary production of aluminium, except the emissions related to the use of fuel. Carbon dioxide emissions result from the electrochemical reduction reaction of alumina with a carbon-based anode. Tetrafluoromethane (CF4) and hexafluoroethane (C2F6) are also produced intermittently.  No greenhouse gases are produced in recycling of aluminium other than from the fuels uses for metal remelting. Sulphur hexafluoride (SF6) emissions are not associated with primary aluminium production; however, casting of some high magnesium containing alloys does result in SF6 emissions and these emissions are accounted for in Section 2C4, Magnesium Production.",
            "alternative_codes": ["2C3"],
            "info": {
                "gases": ["CO2", "CH4", "PFCs", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2C3"],
            },
        },
        "2.C.4": {
            "title": "Magnesium Production",
            "comment": "Magnesium production covers GHG emissions related to both primary magnesium production as well as oxidation protection of magnesium metal during processing (recycling and casting), excluding those emissions relating to fuel use. In the primary production of magnesium, carbon dioxide (CO2) is emitted during calcination of dolomite and magnesite raw materials. Primary production of magnesium from non-carbonate raw materials does not emit carbon dioxide. In the processing of liquid magnesium, cover gases containing carbon dioxide (CO2), sulphur hexafluoride (SF6), the hydrofluorocarbon HFC 134a or the fluorinated ketone FK 5-1-12 ( C3F7C(O)C2F5) may be used. Partial thermal decomposition and/or reaction between these compounds and liquid magnesium generates secondary compounds such as perfluorocarbons (PFCs), which are emitted in addition to unreacted cover gas constituents.",
            "alternative_codes": ["2C4"],
            "info": {
                "gases": [
                    "CO2",
                    "HFCs",
                    "PFCs",
                    "SF6",
                    "other halogenated gases",
                    "NOx",
                    "CO",
                    "NMVOC",
                    "SO2",
                ],
                "corresponding_categories_IPCC1996": ["2C4"],
            },
        },
        "2.C.5": {
            "title": "Lead Production",
            "comment": "Lead production covers production by the sintering/smelting process as well as direct smelting.  Carbon dioxide emissions result as a product of the use of a variety of carbon-based reducing agents in both production processes.",
            "alternative_codes": ["2C5"],
            "info": {"gases": ["CO2"], "corresponding_categories_IPCC1996": ["2C5"]},
        },
        "2.C.6": {
            "title": "Zinc Production",
            "comment": "Zinc production covers emissions from both primary production of zinc from ore as well as recovery of zinc from scrap metals, excluding emissions related to fuel use. Following calcination, zinc metal is produced through one of three methods; 1-electro-thermic distillation, 2-pyro- metallurgical smelting or 3-electrolysis.  If method 1 or 2 is used, carbon dioxide (CO2) is emitted. Method 3 does not result in carbon dioxide emissions. Recovery of zinc from metal scrap often uses the same methods as primary production and may thus produce carbon dioxide emissions, which is included in this section.",
            "alternative_codes": ["2C6"],
            "info": {"gases": ["CO2"], "corresponding_categories_IPCC1996": ["2C5"]},
        },
        "2.C.7": {
            "title": "Other (Please Specify)",
            "alternative_codes": ["2C7"],
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "HFCs",
                    "PFCs",
                    "SF6",
                    "other halogenated gases",
                    "NOx",
                    "CO",
                    "NMVOC",
                    "SO2",
                ],
                "corresponding_categories_IPCC1996": ["2C5"],
            },
        },
        "2.D": {
            "title": "Non-Energy Products from Fuels and Solvent Use",
            "comment": "The use of oil products and coal-derived oils primarily intended for purposes other than combustion.",
            "alternative_codes": ["2D"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["1", "2A5", "2A6", "3"],
            },
            "children": [["2.D.1", "2.D.2", "2.D.3", "2.D.4"]],
        },
        "2.D.1": {
            "title": "Lubricant Use",
            "comment": "Lubricating oils, heat transfer oils, cutting oils and greases.",
            "alternative_codes": ["2D1"],
            "info": {"gases": ["CO2"], "corresponding_categories_IPCC1996": ["1", "3"]},
        },
        "2.D.2": {
            "title": "Paraffin Wax Use",
            "comment": "Oil-derived waxes such as petroleum jelly, paraffin waxes and other waxes.",
            "alternative_codes": ["2D2"],
            "info": {
                "gases": ["CO2", "CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["1", "3"],
            },
        },
        "2.D.3": {
            "title": "Solvent Use",
            "comment": "NMVOC emissions from solvent use e.g. in paint application, degreasing and dry cleaning should be contained here. Emissions from the use of HFCs and PFCs as solvents should be reported under 2F5.",
            "alternative_codes": ["2D3"],
            "info": {
                "gases": ["NMVOC"],
                "corresponding_categories_IPCC1996": ["3A", "3B"],
            },
        },
        "2.D.4": {
            "title": "Other (Please Specify)",
            "comment": "For example, CH4, CO and NMVOC emissions from asphalt production and use (including asphalt blowing), as well as NMVOC emissions from the use of other chemical products than solvents should be contained here, if relevant.",
            "alternative_codes": ["2D4"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2A5", "2A6", "3D"],
            },
        },
        "2.E": {
            "title": "Electronics Industry",
            "alternative_codes": ["2E"],
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "PFCs",
                    "HFCs",
                    "SF6",
                    "other halogenated gases",
                ],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
            "children": [["2.E.1", "2.E.2", "2.E.3", "2.E.4", "2.E.5"]],
        },
        "2.E.1": {
            "title": "Integrated Circuit or Semiconductor",
            "comment": "Emissions of CF4, C2F6, C3F8, c-C4F8, C4F6, C4F8O, C5F8, CHF3, CH2F2, NF3 and SF6 from uses of these gases in Integrated Circuit (IC) manufacturing in rapidly evolving ways and in varying amounts, which depend on product (e.g., memory or logic devices) and equipment manufacturer.",
            "alternative_codes": ["2E1"],
            "info": {
                "gases": [
                    "CO2",
                    "N2O",
                    "PFCs",
                    "HFCs",
                    "SF6",
                    "other halogenated gases",
                ],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.E.2": {
            "title": "TFT Flat Panel Display",
            "comment": "Uses and emissions of predominantly CF4, CHF3, NF3 and SF6 during the fabrication of thin-film transistors (TFTs) on glass substrates for flat panel display manufacture. In addition to these gases, C2F6, C3F8 and c-C4F8 may also be used and emitted during the manufacture of thin and smart displays.",
            "alternative_codes": ["2E2"],
            "info": {
                "gases": ["PFCs", "HFCs", "SF6", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.E.3": {
            "title": "Photovoltaics",
            "comment": "Photovoltaic cell manufacture may use and emit CF4 and C2F6 among others.",
            "alternative_codes": ["2E3"],
            "info": {
                "gases": ["PFCs", "HFCs", "SF6", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.E.4": {
            "title": "Heat Transfer Fluid",
            "comment": "Heat transfer fluids, which include several fully fluorinated carbon compounds (either in pure form or in mixtures) with six or more carbon atoms, used and emitted during IC manufacture, testing and assembly. They are used in chillers, temperature shock testers and vapour phase reflow soldering.",
            "alternative_codes": ["2E4"],
            "info": {
                "gases": ["other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.E.5": {
            "title": "Other (Please Specify)",
            "alternative_codes": ["2E5"],
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "HFCs",
                    "PFCs",
                    "SF6",
                    "other halogenated gases",
                ],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.F": {
            "title": "Product Uses as Substitutes for Ozone Depleting Substances",
            "alternative_codes": ["2F"],
            "info": {
                "gases": ["CO2", "HFCs", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F"],
            },
            "children": [["2.F.1", "2.F.2", "2.F.3", "2.F.4", "2.F.5", "2.F.6"]],
        },
        "2.F.1": {
            "title": "Refrigeration and Air Conditioning",
            "comment": "Refrigeration and air-conditioning systems are usually classified in six application domains or categories.  These categories utilise different technologies such as heat exchangers, expansion devices, pipings and compressors. The six application domains are domestic refrigeration, commercial refrigeration, industrial processes, transport refrigeration, stationary air conditioning, mobile air- conditioning systems. For all these applications, various HFCs are selectively replacing CFCs and HCFCs.  For example, in developed countries, HFC-134a has replaced CFC-12 in domestic refrigeration and mobile air conditioning systems, and blends of HFCs such as R-407C (HFC-32/HFC-125/HFC-134a) and R-410A (HFC-32/HFC- 125) are replacing HCFC-22 mainly in stationary air conditioning.  Other, non HFC substances are used to replace CFCs and HCFCs such as iso-butane in domestic refrigeration or ammonia in industrial refrigeration. HFC- 152a is also being considered for mobile air conditioning in several regions.",
            "alternative_codes": ["2F1"],
            "info": {
                "gases": ["CO2", "HFCs", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F1"],
            },
            "children": [["2.F.1.a", "2.F.1.b"]],
        },
        "2.F.1.a": {
            "title": "Refrigeration and Stationary Air Conditioning",
            "comment": "The application domains are domestic refrigeration, commercial refrigeration, industrial processes, stationary air conditioning.",
            "alternative_codes": ["2F1a"],
            "info": {
                "gases": ["CO2", "HFCs", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F1"],
            },
        },
        "2.F.1.b": {
            "title": "Mobile Air Conditioning",
            "comment": "The application domains are transport refrigeration, mobile air-conditioning systems.",
            "alternative_codes": ["2F1b"],
            "info": {
                "gases": ["CO2", "HFCs", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F1"],
            },
        },
        "2.F.2": {
            "title": "Foam Blowing Agents",
            "comment": "HFCs are being used as replacements for CFCs and HCFCs in foams, particularly in closed-cell insulation applications. Compounds that are being used include HFC- 245fa, HFC-365mfc, HFC-227ea, HFC-134a, and HFC- 152a. The processes and applications for which these various HFCs are being used include insulation boards and panels, pipe sections, sprayed systems and one- component gap filling foams. For open-cell foams, such as integral skin products for automotive steering wheels and facias, emissions of HFCs used as blowing agents are likely to occur during the manufacturing process. In closed- cell foam, emissions not only occur during the manufacturing phase, but usually extend into the in-use phase and often the majority of emission occurs at the end- of-life (de-commissioning losses). Accordingly, emissions can occur over a period of up to 50 years or even longer.",
            "alternative_codes": ["2F2"],
            "info": {
                "gases": ["CO2", "HFCs", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F2"],
            },
        },
        "2.F.3": {
            "title": "Fire Protection",
            "comment": "There are two general types of fire protection (fire suppression) equipment that use greenhouse gases as partial replacements for halons: portable (streaming) equipment, and fixed (flooding) equipment. The non-ozone depleting, industrial gases HFCs, PFCs and more recently a fluoroketone are mainly used as substitutes for halons, typically halon 1301, in flooding equipment.  PFCs played an early role in halon 1301 replacement but current use is limited to replenishment of previously installed systems. HFCs in portable equipment, typically replacing halon 1211, are available but have achieved very limited market acceptance due primarily to their high cost.  PFC use in new portable extinguishers is currently limited to a small amount (few percent) in an HCFC blend.",
            "alternative_codes": ["2F3"],
            "info": {
                "gases": ["CO2", "HFCs", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F3"],
            },
        },
        "2.F.4": {
            "title": "Aerosols",
            "comment": "Most aerosol packages now contain hydrocarbon (HC) as propellants but, in a small fraction of the total, HFCs and PFCs may be used as propellants or solvents. Emissions from aerosols usually occur shortly after production, on average six months after sale. During the use of aerosols, 100% of the chemical is emitted. The 5 main sources are metered dose inhalers (MDIs), personal care products (e.g. hair care, deodorant, shaving cream), household products (e.g. air-fresheners, oven and fabric cleaners), industrial products (e.g. special cleaning sprays such as those for operating electrical contact, lubricants, pipe-freezers) and other general products (e.g. silly string, tire inflators, claxons), although in some regions the use of such general products is restricted. The HFCs currently used as propellants are HFC 134a, HFC 227ea, and HFC 152a. The substance HFC 43 10mee and a PFC, perfluorohexane, are used as solvents in industrial aerosol products.",
            "alternative_codes": ["2F4"],
            "info": {
                "gases": ["HFCs", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F4"],
            },
        },
        "2.F.5": {
            "title": "Solvents",
            "comment": 'HFCs and, to a much lesser extent PFCs, are being used as substitutes for ozone depleting substances (most notably CFC-113). Typical HFCs used are HFC-365mfc and HFC-43-10mee. Use of these fluorinated replacements is much less widespread than the ozone depleting substances they replace. Re-capture and re-use is also much more widely practiced The primary areas of use are precision cleaning, electronics cleaning, metal cleaning and deposition applications. Emissions from aerosols containing solvents should be reported undercategory 2F4 "Aerosols" rather than under this category.',
            "alternative_codes": ["2F5"],
            "info": {
                "gases": ["HFCs", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F5"],
            },
        },
        "2.F.6": {
            "title": "Other Applications (Please Specify)",
            "comment": "The properties of ozone depleting substances have made them attractive for a variety of niche applications not covered in other sub-source categories. These include electronics testing, heat transfer, dielectric fluid and medical applications. The properties of HFCs and PFCs are equally attractive in some of these sectors and they have been adopted as substitutes. There are also some historical uses of PFCs, as well as emerging use of HFCs, in these applications. These applications have leakage rates ranging from 100% emissive in year of application to around 1% per annum.",
            "alternative_codes": ["2F6"],
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "HFCs",
                    "PFCs",
                    "other halogenated gases",
                ],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.G": {
            "title": "Other Product Manufacture and Use",
            "alternative_codes": ["2G"],
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "HFCs",
                    "PFCs",
                    "SF6",
                    "other halogenated gases",
                ],
                "corresponding_categories_IPCC1996": ["2F6", "3D"],
            },
            "children": [["2.G.1", "2.G.2", "2.G.3", "2.G.4"]],
        },
        "2.G.1": {
            "title": "Electrical Equipment",
            "comment": "Electrical equipment is used in the transmission and distribution of electricity above 1 kV. SF6 is used in gas- insulated switchgear (GIS), gas circuit breakers (GCB), gas-insulated transformers (GIT), gas-insulated lines (GIL), outdoor gas-insulated instrument transformers, reclosers, switches, ring main units and other equipment.",
            "alternative_codes": ["2G1"],
            "info": {
                "gases": ["SF6", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
            "children": [["2.G.1.a", "2.G.1.b", "2.G.1.c"]],
        },
        "2.G.1.a": {
            "title": "Manufacture of Electrical Equipment",
            "alternative_codes": ["2G1a"],
            "info": {
                "gases": ["SF6", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.G.1.b": {
            "title": "Use of Electrical Equipment",
            "alternative_codes": ["2G1b"],
            "info": {
                "gases": ["SF6", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.G.1.c": {
            "title": "Disposal of Electrical Equipment",
            "alternative_codes": ["2G1c"],
            "info": {
                "gases": ["SF6", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.G.2": {
            "title": "SF6 and PFCs from Other Product Uses",
            "alternative_codes": ["2G2"],
            "info": {
                "gases": ["SF6", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
            "children": [["2.G.2.a", "2.G.2.b", "2.G.2.c"]],
        },
        "2.G.2.a": {
            "title": "Military Applications",
            "comment": "Military applications include AWACS, which are military reconnaissance planes of the Boeing E-3A type.  In AWACS (and possibly other reconnaissance planes), the SF6 is used as an insulating gas in the radar system.",
            "alternative_codes": ["2G2a"],
            "info": {
                "gases": ["SF6", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.G.2.b": {
            "title": "Accelerators",
            "comment": "Particle accelerators are used for research purposes (at universities and research institutions), for industrial applications (in cross-linking polymers for cable insulation and for rubber parts and hoses), and in medical (radiotherapy) applications.",
            "alternative_codes": ["2G2b"],
            "info": {
                "gases": ["SF6", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.G.2.c": {
            "title": "Other (Please Specify)",
            "comment": "This source includes adiabatic uses, sound-proof glazing, PFCs used as heat transfer fluids in consumer and commercial applications, PFCs used in cosmetic and medical applications, and PFCs and SF6 used as tracers.",
            "alternative_codes": ["2G2c"],
            "info": {
                "gases": ["SF6", "PFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6"],
            },
        },
        "2.G.3": {
            "title": "N2O from Product Uses",
            "alternative_codes": ["2G3"],
            "info": {"gases": ["N2O"], "corresponding_categories_IPCC1996": ["3D"]},
            "children": [["2.G.3.a", "2.G.3.b", "2.G.3.c"]],
        },
        "2.G.3.a": {
            "title": "Medical Applications",
            "comment": "This source covers evaporative emissions of nitrous oxide (N2O) that arise from medical applications (anaesthetic use, analgesic use and veterinary use). N2O is used during anaesthesia for two reasons: a) as an anaesthetic and analgesic and as b) a carrier gas for volatile fluorinated hydrocarbon anaesthetics such as isoflurane, sevoflurane and desflurane.",
            "alternative_codes": ["2G3a"],
            "info": {"gases": ["N2O"], "corresponding_categories_IPCC1996": ["3D"]},
        },
        "2.G.3.b": {
            "title": "Propellant for Pressure and Aerosol Products",
            "comment": "This source covers evaporative emissions of nitrous oxide (N2O) that arise from use as a propellant in aerosol products primarily in food industry. Typical usage is to make whipped cream, where cartridges filled with N2O are used to blow the cream into foam.",
            "alternative_codes": ["2G3b"],
            "info": {"gases": ["N2O"], "corresponding_categories_IPCC1996": ["3D"]},
        },
        "2.G.3.c": {
            "title": "Other (Please Specify)",
            "alternative_codes": ["2G3c"],
            "info": {"gases": ["N2O"], "corresponding_categories_IPCC1996": ["3D"]},
        },
        "2.G.4": {
            "title": "Other (Please Specify)",
            "alternative_codes": ["2G4"],
            "info": {
                "gases": ["CO2", "CH4", "HFCs", "other halogenated gases"],
                "corresponding_categories_IPCC1996": ["2F6", "3D"],
            },
        },
        "2.H": {
            "title": "Other",
            "alternative_codes": ["2H"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2D1", "2D2", "2G"],
            },
            "children": [["2.H.1", "2.H.2", "2.H.3"]],
        },
        "2.H.1": {
            "title": "Pulp and Paper Industry",
            "alternative_codes": ["2H1"],
            "info": {
                "gases": ["CO2", "CH4", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2D1"],
            },
        },
        "2.H.2": {
            "title": "Food and Beverages Industry",
            "alternative_codes": ["2H2"],
            "info": {
                "gases": ["CO2", "CH4", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2D2"],
            },
        },
        "2.H.3": {
            "title": "Other (Please Specify)",
            "alternative_codes": ["2H3"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["2G"],
            },
        },
        "3": {
            "title": "Agriculture, Forestry, and Other Land Use",
            "comment": "Emissions and removals from forest land, cropland, grassland, wetlands, settlements, and other land. Also includes emissions from livestock and manure management, emissions from managed soils, and emissions from liming and urea application. Methods to estimate annual harvested wood product (HWP) variables are also covered in this category.",
            "info": {
                "gases": ["CH4", "N2O", "CO2"],
                "corresponding_categories_IPCC1996": ["4", "5"],
            },
            "children": [["3.A", "3.B", "3.C", "3.D"], ["M.AG", "M.LULUCF"]],
        },
        "3.A": {
            "title": "Livestock",
            "comment": "Methane emissions from enteric fermentation, and methane and nitrous oxide emissions from manure management.",
            "alternative_codes": ["3A"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4"]},
            "children": [["3.A.1", "3.A.2"]],
        },
        "3.A.1": {
            "title": "Enteric Fermentation",
            "comment": "Methane emissions from herbivores as a by-product of enteric fermentation (a digestive process by which carbohydrates are broken down by micro-organisms into simple molecules for absorption into the bloodstream). Ruminant animals (e.g., cattle, sheep) are major sources with moderate amounts produced from non-ruminant animals (e.g., pigs, horses).",
            "alternative_codes": ["3A1"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A"]},
            "children": [
                [
                    "3.A.1.a",
                    "3.A.1.b",
                    "3.A.1.c",
                    "3.A.1.d",
                    "3.A.1.e",
                    "3.A.1.f",
                    "3.A.1.g",
                    "3.A.1.h",
                    "3.A.1.j",
                ],
                [
                    "3.A.1.a",
                    "3.A.1.b",
                    "3.A.1.c",
                    "3.A.1.d",
                    "3.A.1.e",
                    "3.A.1.f",
                    "3.A.1.g",
                    "3.A.1.h",
                    "3.A.1.i",
                    "3.A.1.j",
                ],
            ],
        },
        "3.A.1.a": {
            "title": "Cattle",
            "comment": "Methane emissions from dairy cows and other cattle.",
            "alternative_codes": ["3A1a"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A1"]},
            "children": [["3.A.1.a.i", "3.A.1.a.ii"]],
        },
        "3.A.1.a.i": {
            "title": "Dairy Cows",
            "comment": "Methane emissions from cattle producing milk for commercial exchange and from calves and heifers being grown for dairy purposes.",
            "alternative_codes": ["3A1ai"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A1a"]},
        },
        "3.A.1.a.ii": {
            "title": "Other Cattle",
            "comment": "Methane emissions from all non-dairy cattle including: cattle kept or grown for meat production, draft animals, and breeding animals.",
            "alternative_codes": ["3A1aii"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A1b"]},
        },
        "3.A.1.b": {
            "title": "Buffalo",
            "comment": "Methane emissions from buffalo.",
            "alternative_codes": ["3A1b"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A2"]},
        },
        "3.A.1.c": {
            "title": "Sheep",
            "comment": "Methane emissions from sheep.",
            "alternative_codes": ["3A1c"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A3"]},
        },
        "3.A.1.d": {
            "title": "Goats",
            "comment": "Methane emissions from goats.",
            "alternative_codes": ["3A1d"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A4"]},
        },
        "3.A.1.e": {
            "title": "Camels",
            "comment": "Methane emissions from camels.",
            "alternative_codes": ["3A1e"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A5"]},
        },
        "3.A.1.f": {
            "title": "Horses",
            "comment": "Methane emissions from horses.",
            "alternative_codes": ["3A1f"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A6"]},
        },
        "3.A.1.g": {
            "title": "Mules and Asses",
            "comment": "Methane emissions from mules and asses.",
            "alternative_codes": ["3A1g"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A7"]},
        },
        "3.A.1.h": {
            "title": "Swine",
            "comment": "Methane emissions from swine.",
            "alternative_codes": ["3A1h"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A8"]},
        },
        "3.A.1.j": {
            "title": "Other (Please Specify)",
            "comment": "Methane emissions from other livestock (e.g.  alpacas, llamas, deer, reindeer, etc.).",
            "alternative_codes": ["3A1j"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4A10"]},
        },
        "3.A.2": {
            "title": "Manure Management",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure under low oxygen or anaerobic conditions. These conditions often occur when large numbers of animals are managed in a confined area (e.g. dairy farms, beef feedlots, and swine and poultry farms), where manure is typically stored in large piles or disposed of in lagoons and other types of manure management systems.",
            "alternative_codes": ["3A2"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B"],
            },
            "children": [
                [
                    "3.A.2.a",
                    "3.A.2.b",
                    "3.A.2.c",
                    "3.A.2.d",
                    "3.A.2.e",
                    "3.A.2.f",
                    "3.A.2.g",
                    "3.A.2.h",
                    "3.A.2.i",
                    "3.A.2.j",
                ]
            ],
        },
        "3.A.2.a": {
            "title": "Cattle",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from cattle.",
            "alternative_codes": ["3A2a"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B1"],
            },
            "children": [["3.A.2.a.i", "3.A.2.a.ii"]],
        },
        "3.A.2.a.i": {
            "title": "Dairy Cows",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from dairy cows.",
            "alternative_codes": ["3A2ai"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B1a"],
            },
        },
        "3.A.2.a.ii": {
            "title": "Other Cattle",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from other cattle.",
            "alternative_codes": ["3A2aii"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.A.2.b": {
            "title": "Buffalo",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from buffalo.",
            "alternative_codes": ["3A2b"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B2"],
            },
        },
        "3.A.2.c": {
            "title": "Sheep",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from sheep.",
            "alternative_codes": ["3A2c"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B3"],
            },
        },
        "3.A.2.d": {
            "title": "Goats",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from goats.",
            "alternative_codes": ["3A2d"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B4"],
            },
        },
        "3.A.2.e": {
            "title": "Camels",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from camels.",
            "alternative_codes": ["3A2e"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B5"],
            },
        },
        "3.A.2.f": {
            "title": "Horses",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from horses.",
            "alternative_codes": ["3A2f"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B6"],
            },
        },
        "3.A.2.g": {
            "title": "Mules and Asses",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from mules and assess.",
            "alternative_codes": ["3A2g"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B7"],
            },
        },
        "3.A.2.h": {
            "title": "Swine",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from swine.",
            "alternative_codes": ["3A2h"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B8"],
            },
        },
        "3.A.2.i": {
            "title": "Poultry",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from poultry including chicken, broilers, turkeys, and ducks.",
            "alternative_codes": ["3A2i"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B9"],
            },
        },
        "3.A.2.j": {
            "title": "Other (Please Specify)",
            "comment": "Methane and nitrous oxide emissions from the decomposition of manure from other livestock (e.g. alpacas, llamas, deer, reindeer, fur-bearing animals, ostriches, etc.)",
            "alternative_codes": ["3A2j"],
            "info": {
                "gases": ["CH4", "N2O"],
                "corresponding_categories_IPCC1996": ["4B13"],
            },
        },
        "3.B": {
            "title": "Land",
            "comment": "Emissions and removals from five land use categories (Forest land, Cropland, Grasslands, Settlements, and Other land) except for sources listed under 3C (Aggregate sources and non-CO2 emissions sources on land) . Except for Wetlands, the greenhouse gas inventory involves estimation of changes in carbon stock from five carbon pools (i.e. aboveground biomass, belowground biomass, dead wood, litter, and soil organic matter), as appropriate.",
            "alternative_codes": ["3B"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5"],
            },
            "children": [["3.B.1", "3.B.2", "3.B.3", "3.B.4", "3.B.5", "3.B.6"]],
        },
        "3.B.1": {
            "title": "Forest Land",
            "comment": "Emissions and removals from lands with woody vegetation consistent with thresholds used to define forest land in the national GHG inventory, sub-divided into managed and unmanaged, and possibly also by climatic region, soil type and vegetation type as appropriate. It also includes systems with vegetation that currently fall below, but are expected to later exceed, the threshold values used by a country to define the forest land category.",
            "alternative_codes": ["3B1"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5A", "5C", "5D"],
            },
            "children": [["3.B.1.a", "3.B.1.b"]],
        },
        "3.B.1.a": {
            "title": "Forest Land Remaining Forest Land",
            "comment": "Emissions and removals from managed forests and plantations which have always been under forest land use or other land categories converted to forest over 20 years ago (default assumption).",
            "alternative_codes": ["3B1a"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5A"],
            },
        },
        "3.B.1.b": {
            "title": "Land Converted to Forest Land",
            "comment": "Emissions and removals from lands converted to forest land. Includes conversion of cropland, grassland, wetlands, settlements, and other land to forest land. Even abandoned lands which are regenerating to forest due to human activities are also included.",
            "alternative_codes": ["3B1b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5A", "5C", "5D"],
            },
            "children": [
                ["3.B.1.b.i", "3.B.1.b.ii", "3.B.1.b.iii", "3.B.1.b.iv", "3.B.1.b.v"]
            ],
        },
        "3.B.1.b.i": {
            "title": "Cropland Converted to Forest Land",
            "comment": "Emissions and removals from cropland converted to forest land.",
            "alternative_codes": ["3B1bi"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.1.b.ii": {
            "title": "Grassland Converted to Forest Land",
            "comment": "Emissions and removals from grassland converted to forest land.",
            "alternative_codes": ["3B1bii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.1.b.iii": {
            "title": "Wetlands Converted to Forest Land",
            "comment": "Emissions and removals from wetlands converted to forest land.",
            "alternative_codes": ["3B1biii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.1.b.iv": {
            "title": "Settlements Converted to Forest Land",
            "comment": "Emissions and removals from settlements converted to forest land.",
            "alternative_codes": ["3B1biv"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.1.b.v": {
            "title": "Other Land Converted to Forest Land",
            "comment": "Emissions and removals from other land converted to forest land.",
            "alternative_codes": ["3B1bv"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.2": {
            "title": "Cropland",
            "comment": "Emissions and removals from arable and tillage land, rice fields, and agro-forestry systems where vegetation falls below the thresholds used for the forest land category.",
            "alternative_codes": ["3B2"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": [
                    "4C",
                    "4D",
                    "4F",
                    "5A",
                    "5B",
                    "5D",
                ],
            },
            "children": [["3.B.2.a", "3.B.2.b"]],
        },
        "3.B.2.a": {
            "title": "Cropland Remaining Cropland",
            "comment": "Emissions and removals from cropland that has not undergone any land use change during the inventory period.",
            "alternative_codes": ["3B2a"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["4C", "4D", "4F", "5A", "5D"],
            },
        },
        "3.B.2.b": {
            "title": "Land Converted to Cropland",
            "comment": "Emissions and removals from lands converted to cropland. Includes conversion of forest land, grassland, wetlands, settlements, and other land to cropland.",
            "alternative_codes": ["3B2b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5B", "5D"],
            },
            "children": [
                ["3.B.2.b.i", "3.B.2.b.ii", "3.B.2.b.iii", "3.B.2.b.iv", "3.B.2.b.v"]
            ],
        },
        "3.B.2.b.i": {
            "title": "Forest Land Converted to Cropland",
            "comment": "Emissions and removals from forest land converted to cropland.",
            "alternative_codes": ["3B2bi"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.2.b.ii": {
            "title": "Grassland Converted to Cropland",
            "comment": "Emissions and removals from grassland converted to cropland.",
            "alternative_codes": ["3B2bii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.2.b.iii": {
            "title": "Wetlands Converted to Cropland",
            "comment": "Emissions and removals from wetlands converted to cropland.",
            "alternative_codes": ["3B2biii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.2.b.iv": {
            "title": "Settlements Converted to Cropland",
            "comment": "Emissions and removals from settlements converted to cropland.",
            "alternative_codes": ["3B2biv"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.2.b.v": {
            "title": "Other Land Converted to Cropland",
            "comment": "Emissions and removals from other land converted to cropland.",
            "alternative_codes": ["3B2bv"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.3": {
            "title": "Grassland",
            "comment": "Emissions and removals from rangelands and pasture land that is not considered cropland. It also includes systems with woody vegetation that fall below the threshold values used in the forest land category and are not expected to exceed them, without human intervention. The category also includes all grassland from wild lands to recreational areas as well as agricultural and silvi-pastural systems, subdivided into managed and unmanaged, consistent with national definitions.",
            "alternative_codes": ["3B3"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": [
                    "4D",
                    "4E",
                    "5A",
                    "5B",
                    "5C",
                    "5D",
                ],
            },
            "children": [["3.B.3.a", "3.B.3.b"]],
        },
        "3.B.3.a": {
            "title": "Grassland Remaining Grassland",
            "comment": "Emissions and removals from grassland remaining grassland.",
            "alternative_codes": ["3B3a"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["4D", "4E", "5A", "5D"],
            },
        },
        "3.B.3.b": {
            "title": "Land Converted to Grassland",
            "comment": "Emissions and removals from land converted to grassland.",
            "alternative_codes": ["3B3b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5B", "5C", "5D"],
            },
            "children": [
                ["3.B.3.b.i", "3.B.3.b.ii", "3.B.3.b.iii", "3.B.3.b.iv", "3.B.3.b.v"]
            ],
        },
        "3.B.3.b.i": {
            "title": "Forest Land Converted to Grassland",
            "comment": "Emissions and removals from forest land converted to grassland.",
            "alternative_codes": ["3B3bi"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.3.b.ii": {
            "title": "Cropland Converted to Grassland",
            "comment": "Emissions and removals from cropland converted to grassland.",
            "alternative_codes": ["3B3bii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.3.b.iii": {
            "title": "Wetlands Converted to Grassland",
            "comment": "Emissions and removals from wetlands converted to grassland.",
            "alternative_codes": ["3B3biii"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.3.b.iv": {
            "title": "Settlements Converted to Grassland",
            "comment": "Emissions and removals from settlements converted to grassland.",
            "alternative_codes": ["3B3biv"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.3.b.v": {
            "title": "Other Land Converted to Grassland",
            "comment": "Emissions and removals from other land converted to grassland.",
            "alternative_codes": ["3B3bv"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
        },
        "3.B.4": {
            "title": "Wetlands",
            "comment": "Emissions from land that is covered or saturated by water for all or part of the year (e.g., peatland) and that does not fall into the forest land, cropland, grassland or settlements categories. The category can be subdivided into managed and unmanaged according to national definitions. It includes reservoirs as a managed sub-division and natural rivers and lakes as unmanaged sub-divisions.",
            "alternative_codes": ["3B4"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5A", "5B", "5E", "4D"],
            },
            "children": [["3.B.4.a", "3.B.4.b"]],
        },
        "3.B.4.a": {
            "title": "Wetlands Remaining Wetlands",
            "comment": "Emissions from peatland undergoing peat extraction and from flooded land remaining flooded land.",
            "alternative_codes": ["3B4a"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5A", "5D", "5E", "4D"],
            },
            "children": [["3.B.4.a.i", "3.B.4.a.ii"]],
        },
        "3.B.4.a.i": {
            "title": "Peatlands Remaining Peatlands",
            "comment": "Includes (1) on-site emissions from peat deposits during the extraction phase and (2) off-site emissions from horticultural use of peat. The off-site emissions from the energy use of peat are reported in the Energy Sector and are therefore not included in this category.",
            "alternative_codes": ["3B4ai"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5A", "5E", "4D"],
            },
        },
        "3.B.4.a.ii": {
            "title": "Flooded Land Remaining Flooded Land",
            "comment": "Emissions from flooded land remaining flooded land. Flooded lands are defined as water bodies where human activities have caused changes in the amount of surface area covered by water, typically through water level regulation. Examples of flooded lands include reservoirs for the production of hydroelectricity, irrigation, navigation, etc. Regulated lakes and rivers that have not experienced substantial changes in water area in comparison with the pre-flooded ecosystem are not considered as flooded lands. Some rice paddies are cultivated through flooding of land, but because of the unique characteristics of rice cultivation, rice paddies are addressed in 3C7.",
            "alternative_codes": ["3B4aii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5A", "5E"],
            },
        },
        "3.B.4.b": {
            "title": "Land Converted to Wetlands",
            "comment": "Emissions from land being converted for peat extraction from land converted to wetland.",
            "alternative_codes": ["3B4b"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5B", "5E"],
            },
            "children": [["3.B.4.b.i", "3.B.4.b.ii", "3.B.4.b.iii"]],
        },
        "3.B.4.b.i": {
            "title": "Land Converted for Peat Extraction",
            "comment": "Emissions from land being converted for peat extraction",
            "alternative_codes": ["3B4bi"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5B", "5E"],
            },
        },
        "3.B.4.b.ii": {
            "title": "Land Converted to Flooded Land",
            "comment": "Emissions from land converted to flooded land",
            "alternative_codes": ["3B4bii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5B", "5E"],
            },
        },
        "3.B.4.b.iii": {
            "title": "Land Converted to Other Wetlands",
            "comment": "Emissions from land converted to other wetlands than flooded land and land for peat extraction.",
            "alternative_codes": ["3B4biii"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"],
                "corresponding_categories_IPCC1996": ["5E"],
            },
        },
        "3.B.5": {
            "title": "Settlements",
            "comment": "Emissions and removals from all developed land, including transportation infrastructure and human settlements of any size, unless they are already included under other categories. This should be consistent with national definitions.",
            "alternative_codes": ["3B5"],
            "info": {
                "gases": ["CO2"],
                "corresponding_categories_IPCC1996": ["5A", "5D", "5E", "5B"],
            },
            "children": [["3.B.5.a", "3.B.5.b"]],
        },
        "3.B.5.a": {
            "title": "Settlements Remaining Settlements",
            "comment": "Emissions and removals from settlements that have not undergone any land use change during the inventory period.",
            "alternative_codes": ["3B5a"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.5.b": {
            "title": "Land Converted to Settlements",
            "comment": "Emissions and removals from lands converted to settlements. Includes conversion of forest land, cropland, grassland, wetlands, and other land to settlements.",
            "alternative_codes": ["3B5b"],
            "info": {"gases": ["CO2"]},
            "children": [
                ["3.B.5.b.i", "3.B.5.b.ii", "3.B.5.b.iii", "3.B.5.b.iv", "3.B.5.b.v"]
            ],
        },
        "3.B.5.b.i": {
            "title": "Forest Land Converted to Settlements",
            "comment": "Emissions and removals from forest land converted to settlements.",
            "alternative_codes": ["3B5bi"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.5.b.ii": {
            "title": "Cropland Converted to Settlements",
            "comment": "Emissions and removals from cropland converted to settlements.",
            "alternative_codes": ["3B5bii"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.5.b.iii": {
            "title": "Grassland Converted to Settlements",
            "comment": "Emissions and removals from grassland converted to settlements.",
            "alternative_codes": ["3B5biii"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.5.b.iv": {
            "title": "Wetlands Converted to Settlements",
            "comment": "Emissions and removals from wetlands converted to settlements.",
            "alternative_codes": ["3B5biv"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.5.b.v": {
            "title": "Other Land Converted to Settlements",
            "comment": "Emissions and removals from other land converted to settlements.",
            "alternative_codes": ["3B5bv"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.6": {
            "title": "Other Land",
            "comment": "Emissions and removals from bare soil, rock, ice, and all unmanaged land areas that do not fall into any of the other five categories. It allows the total of identified land areas to match the national area, where data are available.",
            "alternative_codes": ["3B6"],
            "info": {"gases": ["CO2"]},
            "children": [["3.B.6.a", "3.B.6.b"]],
        },
        "3.B.6.a": {
            "title": "Other Land Remaining Other Land",
            "comment": "Emissions and removals from other land that has not undergone any land use change during the inventory period.",
            "alternative_codes": ["3B6a"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.6.b": {
            "title": "Land Converted to Other Land",
            "comment": "Emissions and removals from lands converted to other land. Includes conversion of forest land, cropland, grassland, wetlands, and settlements to other land.",
            "alternative_codes": ["3B6b"],
            "info": {"gases": ["CO2"]},
            "children": [
                ["3.B.6.b.i", "3.B.6.b.ii", "3.B.6.b.iii", "3.B.6.b.iv", "3.B.6.b.v"]
            ],
        },
        "3.B.6.b.i": {
            "title": "Forest Land Converted to Other Land",
            "comment": "Emissions and removals from forest land converted to other land.",
            "alternative_codes": ["3B6bi"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.6.b.ii": {
            "title": "Cropland Converted to Other Land",
            "comment": "Emissions and removals from cropland converted to other land.",
            "alternative_codes": ["3B6bii"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.6.b.iii": {
            "title": "Grassland Converted to Other Land",
            "comment": "Emissions and removals from grassland converted to other land.",
            "alternative_codes": ["3B6biii"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.6.b.iv": {
            "title": "Wetlands Converted to Other Land",
            "comment": "Emissions and removals from wetlands converted to other land.",
            "alternative_codes": ["3B6biv"],
            "info": {"gases": ["CO2"]},
        },
        "3.B.6.b.v": {
            "title": "Settlements Converted to Other Land",
            "comment": "Emissions and removals from settlements converted to other land.",
            "alternative_codes": ["3B6bv"],
            "info": {"gases": ["CO2"]},
        },
        "3.C": {
            "title": "Aggregate Sources and Non-CO2 Emissions Sources on Land",
            "comment": "Includes emissions from activities that are likely to be reported at very high aggregation land level or even country level.",
            "alternative_codes": ["3C"],
            "children": [
                ["3.C.1", "3.C.2", "3.C.3", "3.C.4", "3.C.5", "3.C.6", "3.C.7", "3.C.8"]
            ],
        },
        "3.C.1": {
            "title": "Emissions from Biomass Burning",
            "comment": "Emissions from biomass burning that include N2O and CH4. CO2 emissions are included here only if emissions are not included in 3B categories as carbon stock changes.",
            "alternative_codes": ["3C1"],
            "info": {"gases": ["N2O", "CH4", "CO2"]},
            "children": [["3.C.1.a", "3.C.1.b", "3.C.1.c", "3.C.1.d"]],
        },
        "3.C.1.a": {
            "title": "Biomass Burning In Forest Lands",
            "comment": "Emissions from biomass burning that include N2O and CH4 in forest lands. CO2 emissions are included here only if emissions are not included in 3B1 categories as carbon stock changes.",
            "alternative_codes": ["3C1a"],
            "info": {"gases": ["N2O", "CH4", "CO2"]},
        },
        "3.C.1.b": {
            "title": "Biomass Burning In Croplands",
            "comment": "Emissions from biomass burning that include N2O and CH4 in croplands. CO2 emissions are included here only if emissions are not included in 3B2 categories as carbon stock changes.",
            "alternative_codes": ["3C1b"],
            "info": {"gases": ["N2O", "CH4", "CO2"]},
        },
        "3.C.1.c": {
            "title": "Biomass Burning in Grasslands",
            "comment": "Emissions from biomass burning that include N2O and CH4 in grasslands. CO2 emissions are included here only if emissions are not included in 3B3 categories as carbon stock changes.",
            "alternative_codes": ["3C1c"],
            "info": {"gases": ["N2O", "CH4", "CO2"]},
        },
        "3.C.1.d": {
            "title": "Biomass Burning In All Other Land",
            "comment": "Emissions from biomass burning that include N2O and CH4 in settlements, and all other land. CO2 emissions are included here only if emissions are not included in 3B6 categories as carbon stock changes.",
            "alternative_codes": ["3C1d"],
            "info": {"gases": ["N2O", "CH4", "CO2"]},
        },
        "3.C.2": {
            "title": "Liming",
            "comment": "CO2 emissions from the use of lime in agricultural soils, managed forest soils or lakes.",
            "alternative_codes": ["3C2"],
            "info": {"gases": ["CO2"]},
        },
        "3.C.3": {
            "title": "Urea Application",
            "comment": "CO2 emissions from urea application",
            "alternative_codes": ["3C3"],
            "info": {"gases": ["CO2"]},
        },
        "3.C.4": {
            "title": "Direct N2O Emissions from Managed Soils",
            "comment": "Direct N2O emissions from managed soils from the synthetic N fertilizers application; organic N applied as fertilizer (e.g. animal manure, compost, sewage sludge, rendering waste); urine and dung N deposited on pasture, range and paddock by grazing animals; N in crop residues (above and below ground), including from N-fixing crops and from forages during pasture renewal; N mineralization/immobilization associated with loss/gain of soil organic matter resulting from change of land use or management of mineral soils; and drainage/management of organic soils (i.e., histosols).",
            "alternative_codes": ["3C4"],
            "info": {"gases": ["N2O"], "corresponding_categories_IPCC1996": ["4D"]},
        },
        "3.C.5": {
            "title": "Indirect N2O Emissions from Managed Soils",
            "comment": "Indirect N2O emissions from: (1) the volatilization of N (as NH3 and NOx) following the application of synthetic and organic N fertilizers and /or urine and dung deposition from grazing animals, and the subsequent deposition of the N as ammonium (NH4+) and oxides of N (NOx) on soils and waters, and (2) the leaching and runoff of N from synthetic and organic N fertilizer additions, crop residues, mineralization /immobilization of N associated with loss/gain of soil C in mineral soils through land use change or management practices, and urine and dung deposition from grazing animals, into groundwater, riparian areas and wetlands, rivers and eventually the coastal ocean.",
            "alternative_codes": ["3C5"],
            "info": {"gases": ["N2O"], "corresponding_categories_IPCC1996": ["4D"]},
        },
        "3.C.6": {
            "title": "Indirect N2O Emissions from Manure Management",
            "comment": "Indirect N2O emissions from manure management (activity data amount of nitrogen in the manure excreted).",
            "alternative_codes": ["3C6"],
            "info": {"gases": ["N2O"]},
        },
        "3.C.7": {
            "title": "Rice Cultivations",
            "comment": "Methane (CH4) emissions from anaerobic decomposition of organic material in flooded rice fields. Any N2O emissions from the use of nitrogen-based fertilizers in rice cultivation should be reported under N2O emissions from managed soils.",
            "alternative_codes": ["3C7"],
            "info": {"gases": ["CH4"], "corresponding_categories_IPCC1996": ["4C"]},
        },
        "3.C.8": {
            "title": "Other (Please Specify)",
            "comment": "Other sources of CH4 and N2O emissions on land.",
            "alternative_codes": ["3C8"],
            "info": {"gases": ["N2O", "CH4"]},
        },
        "3.D": {
            "title": "Other",
            "alternative_codes": ["3D"],
            "children": [["3.D.1", "3.D.2"]],
        },
        "3.D.1": {
            "title": "Harvested Wood Products",
            "comment": "CO2 net emissions or removals resulting from Harvest Wood Products.",
            "alternative_codes": ["3D1"],
            "info": {"gases": ["CO2"]},
        },
        "3.D.2": {"title": "Other (Please Specify)", "alternative_codes": ["3D2"]},
        "4": {
            "title": "Waste",
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC", "SO2"]},
            "children": [["4.A", "4.B", "4.C", "4.D", "4.E"]],
        },
        "4.A": {
            "title": "Solid Waste Disposal",
            "comment": "Methane is produced from anaerobic microbial decomposition of organic matter in solid waste disposal sites.  Carbon dioxide (CO2) is also produced but CO2 from biogenic or organic waste sources is covered by the AFOLU Sector. Emissions of halogenated gases should be accounted in IPPU. Long-term storage of carbon in SWDS is reported as an information item.",
            "alternative_codes": ["4A"],
            "info": {
                "gases": ["CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["6A"],
            },
            "children": [["4.A.1", "4.A.2", "4.A.3"]],
        },
        "4.A.1": {
            "title": "Managed Waste Disposal Sites",
            "comment": "A managed solid waste disposal site must have controlled placement of waste (i.e. waste directed to specific deposition areas, a degree of control of scavenging and fires) and will include at least one of the following: cover material; mechanical compaction; or leveling of the waste. This category can be subdivided into aerobic and anaerobic.",
            "alternative_codes": ["4A1"],
            "info": {
                "gases": ["CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["6A1"],
            },
        },
        "4.A.2": {
            "title": "Unmanaged Waste Disposal Sites",
            "comment": "These are all other solid waste disposal sites that do not fall into the above category. This category can be subdivided into deep and shallow.",
            "alternative_codes": ["4A2"],
            "info": {
                "gases": ["CH4", "N2O", "NOx", "NMVOC"],
                "corresponding_categories_IPCC1996": ["6A2"],
            },
        },
        "4.A.3": {
            "title": "Uncategorised Waste Disposal Sites",
            "comment": "Mixture of above 4 A1 and 4 A2. Countries that do not have data on division of managed/unmanaged may use this category.",
            "alternative_codes": ["4A3"],
            "info": {"gases": ["CH4", "N2O", "NOx", "NMVOC"]},
        },
        "4.B": {
            "title": "Biological Treatment of Solid Waste",
            "comment": "Solid waste composting and other biological treatment. Emissions from biogas facilities (anaerobic digestion) with energy production are reported in the Energy Sector (1A4).",
            "alternative_codes": ["4B"],
            "info": {
                "gases": ["CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["6A3"],
            },
        },
        "4.C": {
            "title": "Incineration and Open Burning of Waste",
            "comment": "Incineration of waste and open burning waste, not including waste-to-energy facilities. Emissions from waste burnt for energy are reported under the Energy Sector, 1A. Emissions from burning of agricultural wastes should be reported under AFOLU (3C1).  All non-CO2 greenhouse gases as well as CO2 from fossil waste should be reported here for incineration and open burning.",
            "alternative_codes": ["4C"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["6C"],
            },
            "children": [["4.C.1", "4.C.2"]],
        },
        "4.C.1": {
            "title": "Waste Incineration",
            "comment": "Combustion of solid wastes in controlled incineration facilities.",
            "alternative_codes": ["4C1"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["6C"],
            },
        },
        "4.C.2": {
            "title": "Open Burning of Waste",
            "comment": "Combustion of waste in the open-air or in an open dump.",
            "alternative_codes": ["4C2"],
            "info": {"gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"]},
        },
        "4.D": {
            "title": "Wastewater Treatment and Discharge",
            "comment": "Methane is produced from anaerobic decomposition of organic matter by bacteria in sewage facilities and from food processing and other industrial facilities during wastewater treatment. N2O is also produced by bacteria (denitrification and nitrification) in wastewater treatment and discharge.",
            "alternative_codes": ["4D"],
            "info": {
                "gases": ["CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["6B"],
            },
            "children": [["4.D.1", "4.D.2"]],
        },
        "4.D.1": {
            "title": "Domestic Wastewater Treatment and Discharge",
            "comment": "Treatment and discharge of liquid wastes and sludge from housing and commercial sources (including human waste) through: wastewater sewage systems collection and treatment systems, open pits / latrines, anaerobic lagoons, anaerobic reactors and discharge into surface waters. Emissions from sludge disposed at SWDS are reported under category 4A.",
            "alternative_codes": ["4D1"],
            "info": {
                "gases": ["CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["6B2"],
            },
        },
        "4.D.2": {
            "title": "Industrial Wastewater Treatment and Discharge",
            "comment": "Treatment and discharge of liquid wastes and sludge from industrial processes such as: food processing, textiles, or pulp and paper production. This includes anaerobic lagoons, anaerobic reactors, and discharge into surface waters. Industrial wastewater released into domestic wastewater sewage should be included under 4D1.",
            "alternative_codes": ["4D2"],
            "info": {
                "gases": ["CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["6B1"],
            },
        },
        "4.E": {
            "title": "Other (Please Specify)",
            "comment": "Release of GHGs from other waste handling activities than listed in categories 4A to 4D.",
            "alternative_codes": ["4E"],
            "info": {
                "gases": ["CO2", "CH4", "N2O", "NOx", "CO", "NMVOC"],
                "corresponding_categories_IPCC1996": ["6D"],
            },
        },
        "5": {
            "title": "Other",
            "info": {"corresponding_categories_IPCC1996": ["7"]},
            "children": [["5.A", "5.B"]],
        },
        "5.A": {
            "title": "Indirect N2O Emissions from The Atmospheric Deposition of Nitrogen In NOx and NH3",
            "comment": "Excluding indirect emissions from NOx and NH3 in agriculture which are reported in 3C5 & 3C6.",
            "alternative_codes": ["5A"],
            "info": {"gases": ["N2O"]},
        },
        "5.B": {
            "title": "Other (Please Specify)",
            "comment": "Only use this category exceptionally, for any categories than cannot be accommodated in the categories described above. Include a reference to where a detailed explanation of the category can be found.",
            "alternative_codes": ["5B"],
            "info": {"corresponding_categories_IPCC1996": ["7"]},
        },
        "M.0.EL": {
            "title": "Total emissions excluding LULUCF",
            "comment": "All emissions and removals except for Land Use, Land Use Change, and Forestry",
            "children": [["1", "2", "4", "5", "M.AG"]],
        },
        "M.1.A.2.m": {
            "title": "Other manufacturing (CRF)",
            "comment": "Other Manufacturing (as in CRF tables) (Table 1.A(a)s2, row Other (please specify)",
        },
        "M.1.B.1.c": {
            "title": "Other emission from solid fuels (CRF)",
            "comment": "Table 1s2: c.  Other (as specified in table 1.B.1)",
        },
        "M.LULUCF": {
            "title": "Land Use, Land Use Change, and Forestry",
            "comment": "LULUCF part of AFOLU",
        },
        "M.AG": {
            "title": "Agriculture",
            "comment": "Agricultural part of AFOLU",
            "children": [["3.A", "M.AG.ELV"]],
        },
        "M.AG.ELV": {
            "title": "Agriculture excluding Livestock",
            "comment": "Agricultural part of AFOLU excluding livestock",
        },
        "3.A.1.i": {"title": "Poultry", "comment": "From CRF data"},
        "M.BK": {
            "title": "International Bunkers",
            "comment": "M category as not included in national total in CRF data",
            "children": [["M.BK.A", "M.BK.M"]],
        },
        "M.BK.A": {
            "title": "International Aviation",
            "comment": "International aviation bunkers. same as 1.A.3.a.i, excluded from CRF total",
        },
        "M.BK.M": {
            "title": "International Navigation",
            "comment": "International marine bunkers. same as 1.A.3.d.i, excluded from CRF total",
        },
        "M.MULTIOP": {
            "title": "Multilateral Operations",
            "comment": "Multilateral operations, same as 1.A.5.c, excluded from CRF total",
        },
        "1.A.1.bc": {
            "title": "Petroleum Refining - Manufacture of Solid Fuels and Other Energy Industries",
            "comment": "Sum of 1.A.1.b and 1.A.1.c",
            "children": [["1.A.1.b", "1.A.1.c"]],
        },
        "1.A.3.b_noRES": {
            "title": "Road Transportation no resuspension",
            "comment": "Emissions for Road transportation without the effect from resuspension of particles.",
        },
    },
}
