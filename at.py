#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Weather stations along the Appalachian Trail, using trail towns
provided by Ref. [1].

[1]: http://www.aprs.org/hamtrails/AT-towns.txt
"""

stations = {
    "GA": {
        "Gainesville, GA": "KGVL",      # Gainesville, GA
        "Waleska, GA": "KCNI",          # Canton, GA
        "Jasper, GA": "KCNI",           # Canton, GA
        "Chatsworth, GA": "KDNN",       # Dalton, GA
        "Ellijay, GA": "KDZJ",          # Blairsville, GA
        "Dahlonega, GA": "KGVL",        # Gainesville, GA
        "Cleveland, GA": "KDZJ",        # Blairsville, GA
        "Toccoa, GA": "KTOC",           # Toccoa, GA
        "Blairsville, GA": "KDZJ"       # Blairsville, GA
    },
    "NC": {
        "Franklin, NC": "K1A5",         # Franklin, NC
        "Robbinsville, NC": "KRHP",     # Andrews, NC
        "Waynesville, NC": "KAVL"       # Asheville, NC
    },
    "TN": {
        "Maryville, TN": "KTYS",        # Knoxville, TN
        "Alcoa, TN": "KTYS",            # Knoxville, TN
        "Walland, TN": "KTYS",          # Knoxville, TN
        "Pigeon Forge, TN": "KTYS",     # Knoxville, TN
        "Gatlinburg, TN": "KTYS",       # Knoxville, TN
        "Morristown, TN": "K0VG",       # Jonesville, VA
        "Greeneville, TN": "KTRI",      # Tri-Cities, TN
        "Erwin, TN": "K0A9",            # Elizabethton, TN
        "Johnson City, TN": "KTRI",     # Tri-Cities, TN
        "Bristol, TN": "KVJI",          # Abingdon, VA
        "Mountain City, TN": "KTNB"     # Boone, NC
    },
    "VA": {
        "Abingdon, VA": "KVJI",         # Abingdon, VA
        "Marion, VA": "KMKJ",           # Marion, VA
        "Elk Creek, VA": "KMKJ",        # Marion, VA
        "Wytheville, VA": "KMKJ",       # Marion, VA
        "Bland, VA": "KBLF",            # Bluefield, WV
        "Pearisburg, VA": "KPSK",       # Dublin, VA
        "Pulaski, VA": "KPSK",          # Dublin, VA
        "Blacksburg, VA": "KBCB",       # Blacksburg, VA
        "Salem, VA": "KROA",            # Roanoke, VA
        "Roanoke, VA": "KROA",          # Roanoke, VA
        "Fincastle, VA": "KROA",        # Roanoke, VA
        "Bedford, VA": "KLYH",          # Lynchburg, VA
        "Forest, VA": "KLYH",           # Lynchburg, VA
        "Lynchburg, VA": "KLYH",        # Lynchburg, VA
        "Lexington, VA": "KHSP",        # Hot Springs, VA
        "Waynesboro, VA": "KSHD",       # Staunton, VA
        "Staunton, VA": "KSHD",         # Staunton, VA
        "Charlottesville, VA": "KCHO",  # Charlottesville, VA
        "Harrisonburg, VA": "KSHD",     # Staunton, VA
        "Culpeper, VA": "KCJR",         # Culpeper, VA
        "New Market, VA": "KLUA",       # Luray, VA
        "Warrenton, VA": "KHWY",        # Warrenton, VA
        "Winchester, VA": "KOKV",       # Winchester, VA
        "Bluemont, VA": "KJYO"          # Leesburg, VA
    },
    "WV": {
        "Bluefield, WV": "KBLF",        # Bluefield, WV
        "Princeton, WV": "KBLF",        # Bluefield, WV
        "Union, WV": "KLWB",            # Lewisburg, WV
        "Charles Town, WV": "KMRB",     # Martinsburg, WV
        "Harpers Ferry, WV": "KMRB",    # Martinsburg, WV
        "Charleston, WV": "KCRW",       # Charleston, WV
    },
    "MD":  {
        "Frederick, MD": "KFDK",        # Frederick, MD
        "Hagerstown, MD": "KHGR",       # Hagerstown, MD
        "Thurmont, MD": "KRSP",         # Thurmont, MD
    },
    "PA": {
        "Gettysburg, PA": "KRYT",       # Fountain Dale, PA
        "Chambersburg, PA": "KHGR",     # Hagerstown, MD
        "Mount Holly Springs, PA": "KCXY", # Harrisburg, PA
        "Carlisle, PA": "KCXY",         # Harrisburg, PA
        "Shermans Dale, PA": "KCXY",    # Harrisburg, PA
        "Harrisburg, PA": "KCXY",       # Harrisburg, PA
        "Campbelltown, PA": "KMUI",     # Fort Indiantown Gap, PA
        "Lebanon, PA": "KMUI",          # Fort Indiantown Gap, PA
        "Pine Grove, PA": "KMUI",       # Fort Indiantown Gap, PA
        "Pottsville, PA": "KRDG",       # Reading, PA
        "Tamaqua, PA": "KRDG",          # Reading, PA
        "Northampton, PA": "KABE",      # Allentown, PA
        "Nazareth, PA": "KABE",         # Allentown, PA
        "Tannersville, PA": "KMPO",     # Mt. Pocono, PA
        "Matamoras, PA": "KFWN",        # Sussex, NJ
        "Twin Lakes, PA": "KCXY"        # Harrisburg, PA
    },
    "NJ": {
        "Washington, NJ": "KSMQ",       # Sommerville, NJ
        "Buttzville, NJ": "K12N",       # Andover, NJ
        "Great Meadows, NJ": "K12N",    # Andover, NJ
        "Newton, NJ": "K12N",           # Andover, NJ
        "Vernon, NJ": "KFWN",           # Sussex, NJ
    },
    "NY": {
        "Monroe, NY": "KSWF",           # Newburgh, NY
        "New Windsor, NY": "KSWF",      # Newburgh, NY
        "Yorktown Heights, NY": "KHPN", # White Plains, CT
        "Carmel, NY": "KDXR",           # Danbury, CT
        "Poughkeepsie, NY": "KPOU",     # Poughkeepsie, NY
        "Kingston, NY":"KPOU"           # Poughkeepsie, NY
    },
    "CT": {
        "Bethlehem, CT": "KOXC",        # Oxford, CT
        "Litchfield, CT": "KOXC",       # Oxford, CT
        "Torrington, CT": "KOXC",       # Oxford, CT
        "Winsted, CT": "KBDL",          # Windsor Locks, CT
    },
    "MA": {
        "Pittsfield, MA": "KPSF",       # Pittsfield, MA
        "North Adams, MA": "KAQW"       # North Adams, MA
    },
    "VT": {
        "Marlboro, VT": "KEEN",         # Keene, NH
        "Rutland, VT": "KRUT",          # Rutland, VT
        "Killington, VT": "KRUT",       # Rutland, VT
        "Randolph, VT": "KMPV",         # Montpelier, VT
        "Barre, VT": "KMPV",            # Montpelier, VT
        "Williamstown, VT": "KMPV"      # Montpelier, VT
    },
    "NH": {
        "Hanover, NH": "KLEB",          # Lebanon, NH
        "North Haverhill, NH": "K1V4",  # St. Johnsbury, VT
        "Littleton, NH": "KHIE",        # Whitefield, NH
        "North Conway, NH": "KCWN"      # North Conway, NH
    },
    "ME": {
        "North Woodstock, ME": "KBML",  # Berlin, NH
        "Mexico, ME": "KBML",           # Berlin, NH
        "Wilton, ME": "KWVL",           # Waterville, ME
        "Farmington, ME": "KWVL",       # Waterville, ME
        "Skowhegan, ME": "KWVL",        # Waterville, ME
        "Dexter, ME": "KBGR",           # Bangor, ME
        "Patten, ME": "KMLT"            # Millinocket, ME
    }
}

def airports():
    """Airport weather stations along the Appalachian Trail."""

    x = []
    for k in stations:
        for airport in stations[k].values():
            if not airport in x:
                x.append(airport)

    return x
