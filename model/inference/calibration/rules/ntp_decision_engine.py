def classify_category(GE, GR, GI, GC, I):
    if GE>=96 and GR<=1.5 and GI<=0.5 and GC<=1.0 and I<=0.25:
        return "Cat 1"
    elif GE>=90 and GR<=2.0 and GI<=0.7 and GC<=2.0 and I<=0.30:
        return "Cat 2"
    elif GE>=86 and GR<=3.0 and GI<=0.9 and GC<=2.5 and I<=0.35:
        return "Cat 3"
    else:
        return "Non-compliant"
