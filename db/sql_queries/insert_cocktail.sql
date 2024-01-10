INSERT INTO cocktail (
    cocktail_name,alcoholic,image_url,glass_type,recipe,ingredients,ingredient1,ingredient2,
    ingredient3,ingredient4,ingredient5,ingredient6,ingredient7,ingredient8,ingredient9,
    ingredient10,ingredient11,ingredient12,ingredient13,ingredient14,ingredient15,
    measure1,measure2,measure3,measure4,measure5,measure6,measure7,measure8,measure9,
    measure10,measure11,measure12,measure13,measure14,measure15
) VALUES (
    %(cocktail_name)s, %(alcoholic)s, %(image_url)s, %(glass_type)s, %(recipe)s, %(ingredients)s,
    %(ingredient1)s, %(ingredient2)s, %(ingredient3)s, %(ingredient4)s, %(ingredient5)s, %(ingredient6)s,
    %(ingredient7)s, %(ingredient8)s, %(ingredient9)s, %(ingredient10)s, %(ingredient11)s, %(ingredient12)s,
    %(ingredient13)s, %(ingredient14)s, %(ingredient15)s, %(measure1)s, %(measure2)s, %(measure3)s, 
    %(measure4)s, %(measure5)s, %(measure6)s, %(measure7)s, %(measure8)s, %(measure9)s,
    %(measure10)s, %(measure11)s, %(measure12)s, %(measure13)s, %(measure14)s, %(measure15)s
);