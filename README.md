# PRK_projekt
Semestrální projekt (tvorba compileru), předmět Překladače.

Překladač překládá matematické výrazy do jazyka kalkulačky, která umí počítat součty a násobky integerů a floatů, inverzní hodnotu a logaritmus o základu 10. Vstup podporuje pouze kladná čísla.

calc.py je hlavní program skládající vše dohromady. Vstupem je textový soubor (test_parseru2.txt) a výstup je zapisován do souboru expr_output.txt.
ErrorReporter.py je třída k zachycení errorů lexikální i syntaktické analýzy.
CalcVisitor.py je třída procházející strom a dle získaných lexemů počítá výsledek výrazu.

