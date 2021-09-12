
def stable_match(a_pref: dict, b_pref: dict) -> set:
    a_list = list(a_pref.keys())
    match_dict = {}
    while len(match_dict) != len(a_pref):
        print(a_list)
        for ai in a_list:
            if ai in match_dict.values():
                continue
            print(f"{ai}")
            # obtengo mejor candidato
            bi = a_pref[ai].pop(0)
            # obtengo contrincante
            aj = match_dict.get(bi)

            # se crea pareja si no existe
            if not aj:
                print(f"new match {ai}-{bi}")
                match_dict[bi] = ai
                continue

            bi_pref = b_pref[bi]
            if bi_pref.index(aj) > bi_pref.index(ai):
                print(f"update match {ai}-{bi}")
                match_dict[bi] = ai
                a_list.append(aj)
                continue


    return {(ai, bi) for ai, bi in match_dict.items()}
