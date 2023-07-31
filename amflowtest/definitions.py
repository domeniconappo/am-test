part = {
        "id": "bus",
        "title": "Bus",
        "copies": 1,
        "design_reference": "bus",
        "material": "MTR_PRT_MJF_MAT_PA12",
        "attributes": {
            "prev_step": "Printing",
            "next_step": "shipping",
            "technology": "SLS",
            "order_id": 1,
            "tray": "1",  # group batch is defined by tray
            "target_date": "2023-07-31",
        }
    }


batch = {
    "id": "1",
    "title": "Tray 1",
    "query": "tray=1",
}
