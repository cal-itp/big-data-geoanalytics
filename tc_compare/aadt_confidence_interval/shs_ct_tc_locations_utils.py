# Using Traffic Census locations to help identify the locations
# Also, when available I will also be using the CCTC_Test locations
    # https://tableau.dot.ca.gov/t/TrafficOps/views/CCTV_test/MapSummary?%3Aembed=y&%3Aiid=1&%3AisGuestRedirectFromVizportal=y&%3Aorigin=card_share_link
    
# Back AADT, Peak Month, and Peak Hour usually represents traffic South or West of the count location. 
# Ahead AADT, Peak Month, and Peak Hour usually represents traffic North or East of the count location. Listing of routes with their designated


interstate_605_d7_tc_aadt_locations = [
    {
        'IRWINDALE, LOWER AZUSA ROAD/LOS ANGELES STREET': {
            'location_description': 'IRWINDALE, LOWER AZUSA ROAD/LOS ANGELES STREET',
            'order_number': 0,
            'metadata': {
                'corridor': 'I-605', 'district': 'D7'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['13117'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 160880'],   # northbound stl
                    'zonename_behind': ['San Gabriel River Freeway / 6739504'], # northbound stl
                },
                'bi-directional_1': {
                    'objectid': ['13118'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 160881'],  # southbound stl
                    'zonename_behind': ['San Gabriel River Freeway / 19247825'],  # southbound stl
                }
            }
        },
        'BALDWIN PARK, JCT. RTE. 10': {
            'location_description': 'BALDWIN PARK, JCT. RTE. 10',
            'order_number': 2,
            'metadata': {
                'corridor': 'I-605', 'district': 'D7'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['13113'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 19171162'],  # northbound stl
                    'zonename_behind': ['San Gabriel River Freeway / 164740'], # northbound stl
                },
                'bi-directional_1': {
                    'objectid': ['13114'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 7368478'],  # southbound
                    'zonename_behind': ['San Gabriel River Freeway / 164736'],  # southbound
                }
            }
        },
        'INDUSTRY, VALLEY BOULEVARD': {
            'location_description': 'INDUSTRY, VALLEY BOULEVARD',
            'order_number': 4,
            'metadata': {
                'corridor': 'I-605', 'district': 'D7'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['13111'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 164740'],  # northbound
                    'zonename_behind': ['San Gabriel River Freeway / 703991']   # northbound
                },
                'bi-directional_1': {
                    'objectid': ['13112'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 164736'],  # southbound
                    'zonename_behind': ['San Gabriel River Freeway / 705638']  # southbound
                }
            }
        },
        'INDUSTRY, JCT. RTE. 60': {
            'location_description': 'INDUSTRY, JCT. RTE. 60',
            'order_number': 6,
            'metadata': {
                'corridor': 'I-605', 'district': 'D7'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['13109'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 703991'], # northbound
                    'zonename_behind': ['San Gabriel River Freeway / 1698720'] # northbound
                },
                'bi-directional_1': {
                    'objectid': ['13110'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 705638'], # southbound
                    'zonename_behind': ['San Gabriel River Freeway / 2730673'] # southbound
                }
            }
        },
        'PICO RIVERA, ROSE HILLS ROAD': {
            'location_description': 'PICO RIVERA, ROSE HILLS ROAD',
            'order_number': 8,
            'metadata': {
                'corridor': 'I-605', 'district': 'D7'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['13105'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 8402350'], # northbound
                    'zonename_behind': ['San Gabriel River Freeway / 164212'] # northbound
                },
                'bi-directional_1': {
                    'objectid': ['13106'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 9176481'], # southbound
                    'zonename_behind': ['San Gabriel River Freeway / 673791'] # southbound
                }
            }
        },
        'WHITTIER, JCT. RTE. 72': {
            'location_description': 'WHITTIER, JCT. RTE. 72',
            'order_number': 10,
            'metadata': {
                'corridor': 'I-605', 'district': 'D7'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['13101'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 12790206'], # northbound
                    'zonename_behind': ['San Gabriel River Freeway / 689516'] # northbound
                },
                'bi-directional_1': {
                    'objectid': ['13102'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 8144057'], # southbound
                    'zonename_behind': ['San Gabriel River Freeway / 1283676'] # southbound
                }
            }
        },
        'NORWALK, IMPERIAL HIGHWAY': {
            'location_description': 'NORWALK, IMPERIAL HIGHWAY',
            'order_number': 12,
            'metadata': {
                'corridor': 'I-605', 'district': 'D7'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['13089'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 1292558'], # northbound
                    'zonename_behind': ['San Gabriel River Freeway / 36648843'] # northbound
                },
                'bi-directional_1': {
                    'objectid': ['13090'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 43294'], # southbound
                    'zonename_behind': ['San Gabriel River Freeway / 118798'] # southbound
                }
            }
        },
        'NORWALK, ROSECRANS AVENUE': {
            'location_description': 'NORWALK, ROSECRANS AVENUE',
            'order_number': 14,
            'metadata': {
                'corridor': 'I-605', 'district': 'D7'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['13085'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 18987883'], # northbound
                    'zonename_behind': ['San Gabriel River Freeway / 1292560'] # southbound
                },
                'bi-directional_1': {
                    'objectid': ['13086'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 118696'], # northbound
                    'zonename_behind': ['San Gabriel River Freeway / 23409847'] # southbound
                }
            }
        },
        'NORWALK, ALONDRA BOULEVARD': {
            'location_description': 'NORWALK, ALONDRA BOULEVARD',
            'order_number': 16,
            'metadata': {
                'corridor': 'I-605', 'district': 'D7'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['13084'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 13815791'], # northbound
                    'zonename_behind': ['San Gabriel River Freeway / 4404474'] # northbound
                },
                'bi-directional_1': {
                    'objectid': ['13083'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 118843'], # southbound
                    'zonename_behind': ['San Gabriel River Freeway / 118944'] # southbound
                }
            }
        },
        'CERRITOS, JCT. RTE. 91': {
            'location_description': 'CERRITOS, JCT. RTE. 91',
            'order_number': 18,
            'metadata': {
                'corridor': 'I-605', 'district': 'D7'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['13081'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 4404474'], # northbound
                    'zonename_behind': ['San Gabriel River Freeway / 119733'] # northbound
                },
                'bi-directional_1': {
                    'objectid': ['13082'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['San Gabriel River Freeway / 118944'], # southbound
                    'zonename_behind': ['San Gabriel River Freeway / 45717'] # southbound
                }
            }
        },
    }
]






sr_99_d3_tc_aadt_locations = [
    {
        'BROYLES ROAD': {
            'location_description': 'BROYLES ROAD',
            'order_number': 0,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7879'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 185209'],
                    'zonename_behind': ['CA 99 / 185165']
                }
            }
        },
        'KEEFER ROAD': {
            'location_description': 'KEEFER ROAD',
            'order_number': 1,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7877'],
                    'direction': ['northbound']
                    'zonename_ahead': ['CA 99 / 185159'],
                    'zonename_behind': ['CA 99 / 185106']
                }
            }
        },
        'EATON AVENUE': {
            'location_description': 'EATON AVENUE',
            'order_number': 2,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7873'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 185119'], # northbound
                    'zonename_behind': ['CA 99 / 185088'] # northbound
                },
                'bi-directional_1': {
                    'objectid': ['7874'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 185116'], # southbound
                    'zonename_behind': ['CA 99 / 185087'] # southbound
                }
            }
        },
        'EAST AVENUE': {
            'location_description': 'EAST AVENUE',
            'order_number': 3,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectids': ['7871'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 185088'],
                    'zonename_behind': ['CA 99 / 185041']
                },
                'bi-directional_1': {
                    'objectid': ['7872'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 185087'],
                    'zonename_behind': ['CA 99 / 185045']
                }
            }
        },
        'CHICO, COHASSET HIGHWAY': {
            'location_description': 'CHICO, COHASSET HIGHWAY',
            'order_number': 4,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7869'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 185041'],
                    'zonename_behind': ['CA 99 / 185012']
                },
                'bi-directional_1': {
                    'objectid': ['7870'],
                    'direction': ['southbound']
                    'zonename_ahead': ['CA 99 / 185045'],
                    'zonename_behind': ['CA 99 / 185287']
                }
            }
        },
        'CHICO, EAST FIRST AVENUE': {
            'location_description': 'CHICO, EAST FIRST AVENUE',
            'order_number': 5,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7867'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 185012'], 
                    'zonename_behind': ['Highway 99 / 5232036']
                },
                'bi-directional_1': {
                    'objectid': ['7868'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 185287'], 
                    'zonename_behind': ['Highway 99 / 3236621']
                }
            }
        },
        'CHICO, JCT. RTE. 32 EAST': {
            'location_description': 'CHICO, JCT. RTE. 32 EAST',
            'order_number': 6,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7865'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['Highway 99 / 185312'], 
                    'zonename_behind': ['CA 99 / 185347']
                },
                'bi-directional_1': {
                    'objectid': ['7866'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['Highway 99 / 3236622'], 
                    'zonename_behind': ['CA 99 / 22607112']
                }
            }
        },
        'EAST 20TH STREET': {
            'location_description': 'EAST 20TH STREET',
            'order_number': 7,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7863'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 185347'], 
                    'zonename_behind': ['CA 99 / 22981402']
                },
                'bi-directional_1': {
                    'objectid': ['7864'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 22607112'], 
                    'zonename_behind': ['CA 99 / 185451']
                }
            }
        },
        'CHICO, SKYWAY OVERCROSSING': {
            'location_description': 'CHICO, SKYWAY OVERCROSSING',
            'order_number': 8,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7861'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 22981402'], 
                    'zonename_behind': ['CA 99 / 185556']
                },
                'bi-directional_0': {
                    'objectid': ['7862'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 185451'], 
                    'zonename_behind': ['CA 99 / 185554']
                }
            }
        },
        'NEAL HIGHWAY': {
            'location_description': 'NEAL HIGHWAY',
            'order_number': 9,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7859'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 185597'], 
                    'zonename_behind': ['CA 99 / 185591']
                },
                'bi-directional_1': {
                    'objectid': ['7860'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 185596'], 
                    'zonename_behind': ['CA 99 / 185590']
                }
            }
        },
        'PENTZ ROAD': {
            'location_description': 'PENTZ ROAD',
            'order_number': 10,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7857'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 185591'], 
                    'zonename_behind': ['CA 99 / 185577']
                },
                'bi-directional_1': {
                    'objectid': ['7858'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 185590'], 
                    'zonename_behind': ['CA 99 / 70538']
                }
            }
        },
        'JCT. RTE 149': {
            'location_description': 'JCT. RTE 149',
            'order_number': 11,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7855'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 185577'], 
                    'zonename_behind': ['CA 99 / 16363414']
                },
                'bi-directional_1': {
                    'objectid': ['7856'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 70538'], 
                    'zonename_behind': ['CA 99 / 17021934']
                }
            }
        },
        'NELSON SHIPPEE ROAD': {
            'location_description': 'NELSON SHIPPEE ROAD',
            'order_number': 12,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7853'],
                    'direction': ['bi-directional']
                    'zonename_ahead': ['CA 99 / 712588'], 
                    'zonename_behind': ['CA 99 / 1302938']
                }
            }
        },
        'JCT. RTE. 162 EAST': {
            'location_description': 'JCT. RTE. 162 EAST',
            'order_number': 13,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7851'],
                    'directional': ['bi-direction'],
                    'zonename_ahead': ['CA 99 / 1302938'], 
                    'zonename_behind': ['CA 99;CA 162 / 22187531']
                }
            }
        },
        'JCT. RTE. 162 WEST': {
            'location_description': 'JCT. RTE. 162 WEST',
            'order_number': 14,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7849'],
                    'direction': ['bi-directional']
                    'zonename_ahead': ['CA 99;CA 162 / 22187531'], 
                    'zonename_behind': ['CA 99 / 70189']
                }
            }
        },
        'BIGGS HIGHWAY': {
            'location_description': 'BIGGS HIGHWAY',
            'order_number': 15,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7847'],
                    'direction': ['bi-directional'],
                    'zonename_ahead': ['CA 99 / 70189'], 
                    'zonename_behind': ['CA 99 / 720583']
                }
            }
        },
        'GRIDLEY, SPRUCE STREET': {
            'location_description': 'GRIDLEY, SPRUCE STREET',
            'order_number': 16,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7845'],
                    'direction': ['bi-directional']
                    'zonename_ahead': ['CA 99 / 720583'], 
                    'zonename_behind': ['CA 99 / 713069']
                }
            }
        },
        'GRIDLEY, WILSON STREET': {
            'location_description': 'GRIDLEY, WILSON STREET',
            'order_number': 17,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7843'],
                    'direction': ['bi-directional'],
                    'zonename_ahead': ['CA 99 / 16880739'], 
                    'zonename_behind': ['CA 99 / 693872']
                }
            }
        },
        'LIVE OAK, PENNINGTON ROAD': {
            'location_description': 'LIVE OAK, PENNINGTON ROAD',
            'order_number': 18,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7833'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['Live Oak Boulevard / 185055'], 
                    'zonename_behind': ['Live Oak Boulevard / 185044']
                },
                'bi-directional_1': {
                    'objectid': ['7834'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['Live Oak Boulevard / 185052'],
                    'zonename_behind': ['Live Oak Boulevard / 4270255']
                }
            }
        },
        'ENCINAL ROAD/LIVE OAK BOULEVARD': {
            'location_description': 'ENCINAL ROAD/LIVE OAK BOULEVARD',
            'order_number': 19,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7831'],
                    'direction': ['bi-directional'],
                    'zonename_ahead': ['Live Oak Boulevard / 69780'], 
                    'zonename_behind': ['CA 99 / 690970']
                }
            }
        },
        'EAGER ROAD': {
            'location_description': 'EAGER ROAD',
            'order_number': 20,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_1': {
                    'objectid': ['7830'],
                    'direction': ['southbound']
                    'zonename_ahead': ['CA 99 / 694159'], 
                    'zonename_behind': ['CA 99 / 19182490']
                },
                'bi-directional_0': {
                    'objectid': ['7829'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 711538'], 
                    'zonename_behind': ['CA 99 / 19885831']
                }
            }
        },
        'YUBA CITY, QUEENS AVENUE': {
            'location_description': 'YUBA CITY, QUEENS AVENUE',
            'order_number': 21,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_1': {
                    'objectid': ['7828'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 19182490'], 
                    'zonename_behind': ['CA 99 / 694163']
                },
                'bi-directional_0': {
                    'objectid': ['7827'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 19885831'], 
                    'zonename_behind': ['CA 99 / 185054']
                }
            }
        },
        'YUBA CITY, JCT. RTE. 20': {
            'location_description': 'YUBA CITY, JCT. RTE. 20',
            'order_number': 22,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7825'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 185054'],
                    'zonename_behind': ['CA 99 / 70537']
                },
                'bi-directional_1': {
                    'objectid': ['7826'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 694163'], 
                    'zonename_behind': ['CA 99 / 71210']
                }
            }
        },
        'YUBA CITY, BRIDGE STREET': {
            'location_description': 'YUBA CITY, BRIDGE STREET',
            'order_number': 23,
            'metadata': {'corridor': 'SR-99', 'district': 'D3'},
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7821'],
                    'direction': ['bi-directional'],
                    'zonename_ahead': ['CA 99 / 683549'], 
                    'zonename_behind': ['CA 99 / 1303764']
                }
            }
        },
        'FRANKLIN ROAD': {
            'location_description': 'FRANKLIN ROAD',
            'order_number': 24,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7819'],
                    'direction': ['bi-directional'],
                    'zonename_ahead': ['CA 99 / 1303764'], 
                    'zonename_behind': ['CA 99 / 1302697']
                }
            }
        },
        'YUBA CITY, LINCOLN ROAD': {
            'location_description': 'YUBA CITY, LINCOLN ROAD',
            'order_number': 25,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7817'],
                    'direction': ['bi-directional'],
                    'zonename_ahead': ['CA 99 / 693786'], 
                    'zonename_behind': ['CA 99 / 69539']
                }
            }
        },
        'BOGUE ROAD': {
            'location_description': 'BOGUE ROAD',
            'order_number': 26,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7815'],
                    'direction': ['bi-directional'],
                    'zonename_ahead': ['CA 99 / 69539'], 
                    'zonename_behind': ['CA 99 / 683020']
                }
            }
        },
        'BARRY ROAD': {
            'location_description': 'BARRY ROAD',
            'order_number': 27,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7813'],
                    'direction': ['bi-directional'],
                    'zonename_ahead': ['CA 99 / 683020'], 
                    'zonename_behind': ['CA 99 / 713219']
                }
            }
        },
        'JCT. RTE. 113': {
            'location_description': 'JCT. RTE. 113',
            'order_number': 28,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7809'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 70681'], 
                    'zonename_behind': ['CA 99 / 20383725']
                },
                'bi-directional_1': {
                    'objectid': ['7810'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 19988633'], 
                    'zonename_behind': ['CA 99 / 1305890']
                }
            }
        },
        'FEATHER RIVER BRIDGE': {
            'location_description': 'FEATHER RIVER BRIDGE',
            'order_number': 29,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7805'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 72259'], 
                    'zonename_behind': ['CA 99 / 23862508']
                },
                'bi-directional_1': {
                    'objectid': ['7806'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 62242'], 
                    'zonename_behind': ['CA 99 / 15956877']
                }
            }
        },
        'JCT. RTE. 70 NORTH': {
            'location_description': 'JCT. RTE. 70 NORTH',
            'order_number': 30,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7801'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 15283380'],
                    'zonename_behind': ['CA 99 / 190751']
                },
                'bi-directional_1': {
                    'objectid': ['7802'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['CA 99 / 10474764'], 
                    'zonename_behind': ['CA 99 / 190748']
                }
            }
        },
        'RIEGO ROAD': {
            'location_description': 'RIEGO ROAD',
            'order_number': 31,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7799'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 15435840'], 
                    'zonename_behind': ['CA 99 / 10478428']
                },
                'bi-directional_1': {
                    'objectid': ['7800'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['Golden State Highway / 14677099'], 
                    'zonename_behind': ['Golden State Highway / 17457767']
                }
            }
        },
        'ELVERTA ROAD': {
            'location_description': 'ELVERTA ROAD',
            'order_number': 32,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7793'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 10478428'], 
                    'zonename_behind': ['CA 99 / 190364']
                },
                'bi-directional_1': {
                    'objectid': ['7794'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['Golden State Highway / 62778'], 
                    'zonename_behind': ['Golden State Highway / 190363']
                }
            }
        },
        'ELKHORN BOULEVARD': {
            'location_description': 'ELKHORN BOULEVARD',
            'order_number': 33,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7791'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['CA 99 / 190364'], 
                    'zonename_behind': ['CA 99 / 190201']
                },
                'bi-directional_1': {
                    'objectid': ['7792'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['Golden State Highway / 190363'], 
                    'zonename_behind': ['Golden State Highway / 1700995']
                }
            }
        },
        'SACRAMENTO, 12TH AVENUE': {
            'location_description': 'SACRAMENTO, 12TH AVENUE',
            'order_number': 34,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_1': {
                    'objectid': ['7787'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['South Sacramento Freeway / 193825'], 
                    'zonename_behind': ['South Sacramento Freeway / 192818']
                },
                'bi-directional_1': {
                    'objectid': ['7788'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['South Sacramento Freeway / 193828'],
                    'zonename_behind': ['South Sacramento Freeway / 192822']
                }
            }
        },
         'SACRAMENTO, FRUITRIDGE ROAD': {
             'location_description': 'SACRAMENTO, FRUITRIDGE ROAD',
             'order_number': 35,
             'metadata': {
                 'corridor': 'SR-99', 'district': 'D3'
             },
             'daytype': '0: All Days (M-Su)',
             'nodes': {
                 'bi-directional_0': {
                     'objectid': ['7785'],
                     'direction': ['northbound'],
                     'zonename_ahead': ['South Sacramento Freeway / 192818'], 
                     'zonename_behind': ['South Sacramento Freeway / 5306321']
                 },
                 'bi-directional_1': {
                     'objectid': ['7786'],
                     'direction': ['southbound'],
                     'zonename_ahead': ['South Sacramento Freeway / 192822'], 
                     'zonename_behind': ['South Sacramento Freeway / 20029922']
                 }
             }
         },
        '47TH AVENUE': {
            'location_description': '47TH AVENUE',
            'order_number': 36,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_1': {
                    'objectid': ['7782'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['South Sacramento Freeway / 193001'], 
                    'zonename_behind': ['South Sacramento Freeway / 193022']
                },
                'bi-directional_0': {
                    'objectid': ['7781'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['South Sacramento Freeway / 6282898'],
                    'zonename_behind': ['South Sacramento Freeway / 73027']
                }
            }
        },
        'FLORIN ROAD': {
            'location_description': 'FLORIN ROAD',
            'order_number': 37,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'bi-directional_0': {
                    'objectid': ['7779'],
                    'direction': ['northbound'],
                    'zonename_ahead': ['South Sacramento Freeway / 73027'], 
                    'zonename_behind': ['South Sacramento Freeway / 189284']
                },
                'bi-directional_1': {
                    'objectid': ['7780'],
                    'direction': ['southbound'],
                    'zonename_ahead': ['South Sacramento Freeway / 193022'], 
                    'zonename_behind': ['South Sacramento Freeway / 189279']
                }
            }
        },
        'SACRAMENTO, MACK ROAD': {
            'location_description': 'SACRAMENTO, MACK ROAD',
            'order_number': 38,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'southbound': {
                    'objectid': ['7778'],
                    'zonename_ahead': ['South Sacramento Freeway / 189279'], 
                    'zonename_behind': ['South Sacramento Freeway / 11496158']
                },
                'northbound': {
                    'objectid': ['7777'],
                    'zonename_ahead': ['South Sacramento Freeway / 189284'], 
                    'zonename_behind': ['South Sacramento Freeway / 5251250']
                }
            }
        },
        'DULUTH AVENUE': {
            'location_description': 'DULUTH AVENUE',
            'order_number': 39,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'southbound': {
                    'objectid': ['7774'],
                    'zonename_ahead': ['South Sacramento Freeway / 189277'], 
                    'zonename_behind': ['South Sacramento Freeway / 189188']
                },
                'northbound': {
                    'objectid': ['7773'],
                    'zonename_ahead': ['South Sacramento Freeway / 189275'], 
                    'zonename_behind': ['South Sacramento Freeway / 189132']
                }
            }
        },
        'SHELDON ROAD': {
            'location_description': 'SHELDON ROAD',
            'order_number': 40,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'southbound': {
                    'objectid': ['7768'],
                    'zonename_ahead': ['South Sacramento Freeway / 189188'], 
                    'zonename_behind': ['South Sacramento Freeway / 189132']
                },
                'northbound': {
                    'objectid': ['7767'],
                    'zonename_ahead': ['South Sacramento Freeway / 188302'], 
                    'zonename_behind': ['South Sacramento Freeway / 188301']
                }
            }
        },
        'LAGUNA BOULEVARD/ BOND ROAD': {
         'location_description': 'LAGUNA BOULEVARD/ BOND ROAD',
         'order_number': 41,
         'metadata': {
             'corridor': 'SR-99', 'district': 'D3'
         },
         'daytype': '0: All Days (M-Su)',
         'nodes': {
             'southbound': {
                 'objectid': ['7766'],
                 'zonename_ahead': ['South Sacramento Freeway / 188302'], 
                 'zonename_behind': ['South Sacramento Freeway / 1302576']
             },
             'northbound': {
                 'objectid': ['7765'],
                 'zonename_ahead': ['South Sacramento Freeway / 188301'], 
                 'zonename_behind': ['South Sacramento Freeway / 188510']
             }
         }
        },
        'ELK GROVE BOULEVARD': {
            'location_description': 'ELK GROVE BOULEVARD',
            'order_number': 42,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'southbound': {
                    'objectid': ['7764'],
                    'zonename_ahead': ['South Sacramento Freeway / 1302576'], 
                    'zonename_behind': ['South Sacramento Freeway / 188084']
                },
                'northbound': {
                    'objectid': ['7763'],
                    'zonename_ahead': ['South Sacramento Freeway / 188510'], 
                    'zonename_behind': ['South Sacramento Freeway / 1305508']
                }
            }
        },
        'GRANT LINE ROAD': {
            'location_description': 'GRANT LINE ROAD',
            'order_number': 43,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'southbound': {
                    'objectid': ['7762'],
                    'zonename_ahead':['South Sacramento Freeway / 188084'], 
                    'zonename_behind': ['South Sacramento Freeway / 22309324']
                },
                'northbound': {
                    'objectid': ['7761'],
                    'zonename_ahead': ['South Sacramento Freeway / 1305508'], 
                    'zonename_behind': ['South Sacramento Freeway / 188730']
                }
            }
        },
        'DILLARD ROAD': {
            'location_description': 'DILLARD ROAD',
            'order_number': 44,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'southbound': {
                    'objectid': ['7758'],
                    'zonename_ahead': ['South Sacramento Freeway / 188721'], 
                    'zonename_behind': ['South Sacramento Freeway / 188716']
                },
                'northbound': {
                    'objectid': ['7757'],
                    'zonename_ahead': ['South Sacramento Freeway / 188730'], 
                    'zonename_behind': ['South Sacramento Freeway / 70493']
                }
            }
        },
        'ARNO ROAD': {
            'location_description': 'ARNO ROAD',
            'order_number': 45,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'southbound': {
                    'objectid': ['7756'],
                    'zonename_ahead': ['South Sacramento Freeway / 188716'], 
                    'zonename_behind': ['South Sacramento Freeway / 9947986']
                },
                'northbound': {
                    'objectid': ['7755'],
                    'zonename_ahead': ['South Sacramento Freeway / 70493'], 
                    'zonename_behind': ['South Sacramento Freeway / 10980779']
                }
            }
        },
        'JCT. RTE. 104 EAST': {
            'location_description': 'JCT. RTE. 104 EAST',
            'order_number': 46,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'southbound': {
                    'objectid': ['7752'],
                    'zonename_ahead': ['South Sacramento Freeway / 9947988'], 
                    'zonename_behind': ['South Sacramento Freeway / 9947991']
                },
                'northbound': {
                    'objectid': ['7751'],
                    'zonename_ahead': ['South Sacramento Freeway / 10980777'], 
                    'zonename_behind': ['South Sacramento Freeway / 10980774']
                }
            }
        },
        'WALNUT STREET CONNECTION': {
            'location_description': 'WALNUT STREET CONNECTION',
            'order_number': 47,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'southbound': {
                    'objectid': ['7750'],
                    'zonename_ahead': ['South Sacramento Freeway / 9947991'], 
                    'zonename_behind': ['South Sacramento Freeway / 9947994']
                },
                'northbound': {
                    'objectid': ['7749'],
                    'zonename_ahead': ['South Sacramento Freeway / 10980774'], 
                    'zonename_behind': ['South Sacramento Freeway / 22215110']
                }
            }
        },
        'GALT, C STREET': {
            'location_description': 'GALT, C STREET',
            'order_number': 48,
            'metadata': {
                'corridor': 'SR-99', 'district': 'D3'
            },
            'daytype': '0: All Days (M-Su)',
            'nodes': {
                'southbound': {
                    'objectid': ['7744'],
                    'zonename_ahead': ['South Sacramento Freeway / 21487462'], 
                    'zonename_behind': ['South Sacramento Freeway / 21487460']
                },
                'northbound': {
                    'objectid': ['7743'],
                    'zonename_ahead': ['South Sacramento Freeway / 22215115'], 
                    'zonename_behind': ['South Sacramento Freeway / 22215117']
                }
            }
        }
    },
]
