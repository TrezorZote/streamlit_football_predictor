
#{
#  "Team Name": [home_goals_scored_per_game,
#                away_goals_scored_per_game,
 #               home_goals_conceded_per_game,
 #               away_goals_conceded_per_game]}
#

pl_team_stats = {
    "Arsenal":      [2.38, 1.50, 0.62, 0.75],
    "Aston Villa":  [1.46, 1.38, 0.76, 1.3],   # partial data
    "Bournemouth":  [1.92, 1.23, 1.00, 1.69],
    "Brentford":    [1.92, 1.23, 1.00, 1.69],
    "Brighton":     [1.92, 1.23, 1.08, 1.58],
    "Chelsea":      [1.67, 1.92, 1.08, 1.15],
    "Crystal Palace":[0.92, 1.15, 1.25, 1.17],
    "Everton":      [1.23, 1.0, 1.38, 0.92],
    "Leeds United": [1.69, 1.00, 1.38, 2.08],
    "Liverpool":    [1.61, 1.53, 1.00, 1.61],
    "Manchester City":[2.45, 1.69, 0.66, 1.2],
    "Manchester United":[1.92, 1.75, 1.15, 1.75],
    "Newcastle United":[1.85, 0.92, 1.50, 1.34],
    "Nottingham Forest":[1.08, 0.92, 1.50, 1.54],
    "Sunderland":[1.60, 1.54, 0.76, 1.53],
    "Tottenham Hotspur":[1.00, 1.46, 1.33, 1.46],
    "West Ham United":[1.33, 1.00, 2.17, 1.69],
    "Wolverhampton Wanderers":[0.85, 0.42, 2.15, 1.67],
    "Fulham":       [1.69, 1.08, 1.23, 1.75],
    "Bournemouth":  [1.92, 1.23, 1.00, 1.69]
}

championship_team_stats = {
    "Coventry City":        [1.72, 1.28, 1.10, 1.22],
    "Ipswich Town":         [1.88, 1.36, 0.94, 1.18],
    "Hull City":            [1.31, 1.80, 1.20, 1.60],
    "Middlesbrough":        [1.75, 1.67, 1.10, 1.36],
    "Millwall":             [1.88, 1.53, 1.30, 1.40],
    "Wrexham":              [1.50, 1.53, 1.30, 1.50],
    "Southampton":          [1.73, 1.18, 1.30, 1.40],
    "Birmingham City":      [1.94, 0.94, 1.10, 1.50],
    "Derby County":         [1.13, 1.80, 1.50, 1.70],
    "Watford":              [1.81, 1.00, 1.30, 1.60],
    "Queens Park Rangers":  [1.73, 1.13, 1.20, 1.40],
    "Stoke City":           [1.40, 1.38, 1.40, 1.50],
    "Swansea City":         [1.75, 0.93, 1.20, 1.70],
    "Norwich City":         [1.07, 1.35, 1.30, 1.50],
    "Sheffield United":     [1.53, 1.00, 1.10, 1.50],
    "Charlton Athletic":    [1.57, 0.88, 1.40, 1.60],
    "West Brom":            [1.53, 0.65, 1.30, 1.70],
    "Portsmouth":           [1.47, 0.79, 1.40, 1.80],
    "Leicester City":       [1.38, 1.00, 1.20, 1.50],
    "Blackburn Rovers":     [0.88, 1.20, 1.60, 1.70],
    "Oxford United":        [0.94, 0.81, 1.50, 1.80],
    "Sheffield Wednesday":  [0.25, 0.47, 2.00, 1.93],
    "Bristol City":         [1.50, 1.47, 1.30, 1.60],
    "Southend United":      [1.00, 1.00, 1.50, 1.50],  # approximate
}



la_liga_team_stats = {
    "Barcelona":          [2.27, 2.00, 0.45, 1.50],
    "Real Madrid":        [2.27, 2.00, 0.64, 0.92],
    "Villarreal":         [2.25, 1.60, 0.83, 1.40],
    "Celta de Vigo":      [1.42, 1.18, 1.25, 0.91],
    "Valencia":           [1.25, 0.73, 1.08, 2.18],
    "Mallorca":           [1.64, 0.83, 1.27, 1.92],
    "Real Betis":         [2.00, 1.25, 1.09, 1.33],
    "Getafe":             [0.73, 0.83, 0.82, 1.50],
    "Levante":            [1.10, 1.25, 2.00, 1.50],
    "Real Oviedo":        [1.00, 0.36, 1.00, 2.09],
    "Deportivo Alaves":   [1.17, 0.55, 1.08, 1.45],
    "Athletic Club Bilbao":[1.25, 0.91, 1.17, 1.73],
    "Rayo Vallecano":     [0.80, 0.83, 0.90, 1.75],
    "Elche":              [1.17, 1.00, 1.08, 2.00],
    "Osasuna":            [1.82, 0.67, 1.18, 1.25],
    "Real Sociedad":      [1.75, 1.09, 1.42, 1.27], 
    "Sevilla":            [1.45, 1.18, 1.50, 1.82], 
    "Atletico Madrid":    [2.36, 1.09, 0.64, 0.91],
 
}

spanish_segunda_team_stats = {
    "Racing Santander":       [2.27, 2.00, 1.08, 1.15],
    "Almeria":                [2.30, 1.55, 1.20, 1.37],
    "Castellon":              [2.20, 1.20, 0.75, 1.20],
    "Deportivo La Coruna":    [1.50, 1.82, 1.08, 1.27],
    "Malaga CF":              [1.90, 1.00, 1.15, 1.30],
    "Sporting Gijon":         [1.36, 1.10, 1.25, 1.32],
    "Real Sociedad II":       [1.45, 1.20, 1.08, 1.30],
    "Cordoba":                [1.30, 1.20, 1.20, 1.25],
    "Las Palmas":             [1.55, 0.90, 0.62, 1.10],
    "AD Ceuta FC":            [1.40, 1.00, 1.10, 1.40],
    "Burgos CF":              [1.00, 1.40, 0.95, 1.15],
    "Cadiz CF":               [1.27, 1.10, 1.10, 1.30],
    "Granada CF":             [1.30, 1.00, 1.15, 1.27],
    "Huesca":                 [1.30, 0.60, 1.10, 1.50],
    "FC Andorra":             [1.10, 1.09, 1.15, 1.25],
    "Valladolid":             [1.18, 0.89, 1.00, 1.21],
    "Leganes":                [0.67, 1.27, 1.00, 1.30],
    "Real Zaragoza":          [0.80, 1.09, 1.10, 1.27],
    "Cultural Leonesa":       [0.60, 1.45, 1.20, 1.40],
    "SD Eibar":               [0.42, 1.37, 1.20, 1.50],
}

serie_a_team_stats = {
    "Inter Milan":    [2.75, 2.00, 0.83, 0.82],
    "AC Milan":       [2.18, 1.75, 0.82, 0.67],
    "Juventus":       [1.55, 1.17, 0.73, 0.83],
    "AS Roma":        [1.55, 1.45, 0.55, 0.67],
    "Napoli":         [1.55, 1.25, 0.82, 1.08],
    "Como":           [1.67, 1.55, 0.58, 0.82],
    "Atalanta":       [1.54, 1.09, 0.77, 1.00],
    "Lazio":          [1.40, 1.00, 1.17, 0.64],
    "Bologna":        [1.33, 1.00, 1.18, 1.42],
    "Sassuolo":       [1.00, 1.25, 1.58, 1.25],
    "Udinese":        [1.33, 1.00, 1.33, 1.64],
    "Cagliari":       [1.15, 1.10, 1.18, 1.50],
    "Genoa":          [1.20, 1.10, 1.38, 1.73],
    "Torino":         [1.00, 1.00, 1.67, 1.83],
    "Cremonese":      [1.00, 0.77, 1.36, 1.38],
    "Fiorentina":     [1.42, 0.83, 1.58, 1.58],
    "Pisa":           [0.58, 1.33, 1.17, 2.17],
    "Verona":         [0.92, 0.58, 1.58, 1.83],
    "Lecce":          [0.92, 0.75, 1.25, 1.36],
    "Parma":          [0.67, 0.67, 1.42, 1.18],
}

ligue1_team_stats = {
    "Paris Saint Germain":     [2.10, 1.40, 0.44, 1.09],
    "Marseille":               [1.80, 1.30, 1.10, 1.10],
    "Lens":                    [1.60, 1.10, 0.45, 1.20],
    "Lille":                   [1.40, 1.00, 1.20, 1.64],
    "Lyon":                    [1.35, 0.95, 0.70, 1.18],
    "Strasbourg":              [1.30, 0.90, 0.70, 1.80],
    "Monaco":                  [1.50, 1.10, 1.64, 1.67],
    "Toulouse":                [1.40, 1.00, 1.36, 0.89],
    "Nice":                    [1.45, 1.10, 1.40, 2.40],
    "Nantes":                  [1.30, 1.00, 2.00, 1.50],
    "Auxerre":                 [1.10, 0.70, 1.20, 1.70],
    "Metz":                    [1.20, 0.90, 1.50, 2.82],
    "Paris FC":                [1.20, 1.10, 1.70, 1.70],
    "Stade Brestois 29":       [1.25, 0.95, 1.18, 2.00],
    "Lorient":                 [1.30, 1.10, 1.60, 1.55],
    "Le Havre":                [1.10, 0.80, 0.90, 1.60],
    "Angers":                  [1.15, 0.85, 1.20, 1.30],
    "Stade Rennais":           [1.35, 1.10, 1.10, 2.09]
}


bundesliga_team_stats = {
    "Bayern Munich":         [4.09, 3.40, 0.91, 0.90],
    "TSG Hoffenheim":        [2.40, 1.82, 1.30, 1.36],
    "RB Leipzig":            [2.30, 1.55, 1.30, 1.36],
    "Borussia Dortmund":     [2.20, 1.91, 0.80, 1.09],
    "Bayer Leverkusen":      [2.00, 1.90, 1.00, 1.70],
    "SC Freiburg":           [1.90, 1.30, 1.10, 1.57],
    "FC Köln":               [1.73, 1.11, 1.55, 1.62],
    "Eintracht Frankfurt":   [1.70, 2.18, 1.80, 2.55],
    "VfB Stuttgart":         [1.40, 2.18, 1.10, 1.55],
    "SV Werder Bremen":      [1.20, 0.91, 1.80, 1.86],
    "FC Augsburg":           [1.36, 1.00, 1.73, 1.86],
    "Hamburger SV":          [1.50, 1.10, 1.10, 1.10],  # source incomplete
    "1. FC Heidenheim":      [0.82, 0.90, 2.18, 2.30],
    "Union Berlin":          [1.00, 1.00, 1.55, 1.62],
    "FSV Mainz 05":          [1.09, 1.30, 1.18, 2.00],
    "Borussia Mönchengladbach":[1.33, 1.22, 1.30, 1.30],
    "VfL Wolfsburg":         [1.55, 1.20, 2.09, 2.10],
    "FC St. Pauli":          [1.00, 0.80, 1.00, 1.00],
}

bundesliga2_team_stats = {
    "SV Darmstadt 98":       [1.50, 1.21, 1.40, 1.20],
    "Hannover 96":          [1.40, 1.15, 1.30, 1.36],
    "SV Elversberg":        [1.45, 1.12, 1.50, 1.42],
    "1. FC Kaiserslautern": [1.30, 1.06, 1.42, 1.30],
    "1. FC Magdeburg":      [1.25, 1.00, 1.36, 1.12],
    "SC Paderborn 07":      [1.40, 1.06, 1.30, 1.18],
    "Arminia Bielefeld":    [1.50, 1.00, 1.60, 1.40],
    "Greuther Fürth":       [1.30, 1.06, 1.58, 1.42],
    "Dynamo Dresden":       [1.30, 1.09, 1.40, 1.50],
    "Karlsruher SC":        [1.34, 1.06, 1.42, 1.30],
    "Preußen Münster":      [1.25, 1.10, 1.50, 1.30],
    "Eintracht Braunschweig":[1.30, 1.10, 1.45, 1.06],
    "VfL Bochum":           [1.40, 1.10, 1.30, 1.18],
    "Holstein Kiel":        [1.28, 1.06, 1.40, 1.34],
    "1. FC Nürnberg":       [1.30, 1.12, 1.36, 1.26],
    "Fortuna Düsseldorf":   [1.30, 1.04, 1.38, 1.30],
    "Hertha BSC":           [1.15, 1.06, 1.70, 1.20],
    "FC Schalke 04":        [1.25, 1.00, 1.18, 1.06]
}

eredivisie_team_stats = {
    "Ajax":           [2.24, 2.05, 0.82, 0.88],
    "PSV Eindhoven":  [2.40, 2.15, 0.91, 0.90],
    "Feyenoord":      [2.10, 1.90, 0.88, 0.95],
    "AZ Alkmaar":     [1.90, 1.65, 1.05, 1.10],
    "NEC Nijmegen":   [2.00, 1.75, 1.15, 1.20],
    "Twente":         [1.85, 1.55, 1.10, 1.25],
    "Utrecht":        [1.65, 1.40, 1.30, 1.40],
    "Heerenveen":     [1.60, 1.45, 1.35, 1.45],
    "Volendam":       [1.55, 1.15, 1.45, 1.55],
    "Fortuna Sittard": [1.50, 1.10, 1.55, 1.60],
    "Heracles Almelo": [1.75, 1.40, 1.61, 1.50],
    "PEC Zwolle":     [1.50, 1.05, 1.30, 1.50],
    "Excelsior":      [1.45, 1.00, 1.12, 1.50],
    "Sparta Rotterdam": [1.55, 1.30, 1.25, 1.35],
    "Go Ahead Eagles": [1.50, 1.30, 1.20, 1.30],
    "Groningen":      [1.40, 1.20, 1.25, 1.40],
    "Willem II":      [1.30, 1.00, 1.45, 1.55],
    "Telstar":        [1.35, 0.95, 1.30, 1.50]
}


swiss_league_stats = {
    "Thun":             [2.00, 2.50, 1.30, 1.11],  # high scoring overall, strong away scoring
    "FC Lugano":        [2.09, 1.50, 1.22, 1.11],  # solid home, moderate away
    "St. Gallen":       [1.64, 1.91, 1.10, 1.25],  # good scoring away
    "Basel":            [1.58, 1.82, 1.17, 1.40],  # balanced attack/defense
    "FC Sion":          [1.58, 1.36, 1.22, 1.67],  # modest offense/defense
    "Young Boys":       [1.82, 1.08, 1.50, 2.45],  # fairly high home scoring, weaker defense away
    "Lausanne Sports":  [1.33, 1.18, 1.70, 1.10],  # average scoring/conceding
    "FC Luzern":        [0.92, 1.33, 2.20, 1.73],  # lower home scoring, weaker defense
    "Servette FC":      [0.92, 1.27, 1.89, 2.00],  # lower scoring, higher conceded
    "FC Zurich":        [1.18, 1.00, 1.90, 1.78],  # moderate rates
    "Grasshopper":      [0.92, 0.75, 1.50, 2.10],  # lower scoring, higher conceded
    "FC Winterthur":    [0.82, 0.45, 2.44, 3.00],  # weakest numbers
}


danish_superliga_stats = {
    "FC Midtjylland":    [2.40, 1.67, 1.40, 0.89],
    "AGF Aarhus":        [2.20, 2.33, 1.60, 1.22],
    "Nordsjaelland":     [1.80, 1.00, 1.10, 2.44],
    "SønderjyskE":       [1.89, 1.20, 1.00, 1.67],
    "Brøndby IF":        [1.70, 1.67, 1.20, 1.14],
    "Odense BK":         [1.56, 1.20, 1.80, 1.96],
    "Viborg":            [1.44, 1.40, 1.80, 1.10],
    "FC København":      [1.44, 1.50, 1.70, 1.78],
    "Vejle BK":          [1.10, 0.22, 1.60, 2.44],
    "Silkeborg":         [1.10, 0.89, 1.40, 2.56],
    "Randers FC":        [1.22, 0.90, 1.80, 1.20],
    "Fredericia":        [0.78, 1.00, 2.22, 2.60],
}


saudi_pro_league_stats = {
    "Al Hilal":      [2.63, 2.00, 0.89, 1.11],
    "Al Nassr":      [2.55, 1.85, 0.89, 1.11],
    "Al Qadsiah":    [2.25, 1.75, 1.00, 1.33],
    "Al Khaleej":    [2.10, 1.60, 1.00, 1.33],
    "Al Taawoun":    [2.00, 1.55, 1.11, 1.22],
    "Al Ahli":       [1.85, 1.40, 0.67, 0.25],
    "Al Ittihad":    [1.70, 1.30, 1.11, 1.44],
    "Al Ettifaq":    [1.55, 1.25, 1.56, 1.78],
    "Damac":         [1.45, 1.10, 1.50, 2.10],
    "Al Hazm":       [1.40, 1.05, 2.44, 1.33],
    "Al Kholood":    [1.40, 1.05, 2.20, 1.63],
    "Al Riyadh":     [1.35, 0.95, 1.56, 2.67],
    "Al Shabab":     [1.30, 1.10, 1.63, 1.20],
    "NEOM SC":       [1.30, 1.05, 1.70, 1.38],
    "Al Fayha":      [1.25, 0.92, 1.11, 2.44],
    "Al Najma":      [1.15, 0.85, 2.11, 2.00],
    "Al Feiha":      [1.10, 0.90, 1.11, 2.44],
    "Al Okhdood":    [1.10, 0.95, 1.78, 2.00],
}

primeira_liga_team_stats = {
    "Sporting CP":   [3.33, 2.20, 0.40, 0.70],
    "Benfica":       [2.30, 2.11, 0.70, 0.40],
    "FC Porto":      [2.11, 2.10, 0.22, 0.36],
    "Estoril":       [2.10, 2.00, 1.45, 1.90],
    "SC Braga":      [2.11, 1.80, 0.78, 1.00],
    "Nacional":      [1.78, 1.00, 1.89, 1.18],
    "Moreirense":    [1.56, 1.09, 1.30, 1.45],
    "GIL Vicente":   [1.33, 1.20, 0.70, 0.91],
    "Famalicao":     [1.60, 0.89, 0.80, 1.10],
    "Estrela Amadora":[1.30, 1.10, 1.55, 2.00],
    "Arouca":        [1.10, 1.20, 2.09, 2.30],
    "Rio Ave":       [1.00, 1.20, 1.80, 2.00],
    "Casa Pia":      [1.11, 1.00, 1.90, 2.00],
    "Guimaraes":     [1.36, 0.67, 1.27, 1.60],
    "Alverca":       [0.91, 1.11, 1.36, 2.11],
    "Santa Clara":   [0.82, 0.78, 1.09, 1.40],
    "AVS":           [0.70, 0.78, 2.09, 3.11],
    "Tondela":       [0.67, 0.60, 1.30, 2.00],
}

turkish_super_lig_stats = {
    "Galatasaray":       [1.65, 1.27, 0.80, 1.00],  # strong scoring + defense
    "Fenerbahce":        [1.60, 1.55, 0.90, 0.85],  # high scoring
    "Trabzonspor":       [1.50, 1.45, 0.85, 1.00],  # solid both
    "Besiktas":          [1.45, 1.40, 1.00, 1.10],
    "Istanbul Basaksehir":[1.40, 1.35, 1.10, 1.15],
    "Gaziantep":         [1.30, 1.25, 1.15, 1.20],
    "Goztepe":           [1.25, 1.20, 0.90, 1.10],
    "Genclerbirligi":    [1.20, 1.10, 1.20, 1.30],
    "Konyaspor":         [1.18, 1.15, 1.22, 1.30],
    "Rizespor":          [1.15, 1.10, 1.25, 1.20],
    "Samsunspor":        [1.10, 1.08, 1.40, 1.35],
    "Alanyaspor":        [1.05, 1.00, 1.30, 1.25],
    "Antalyaspor":       [1.02, 0.98, 1.38, 1.30],
    "Karagumruk":        [0.95, 0.92, 1.45, 1.40],
    "Eyupspor":          [0.90, 0.88, 1.50, 1.45],
    "Kayserispor":       [0.85, 0.82, 1.80, 1.60],
    "Kocaelispor":       [0.80, 0.75, 1.60, 1.55],
    "Kasimpasa":         [0.78, 0.75, 1.70, 1.65],
}
