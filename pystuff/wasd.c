#include <stdio.h>

int main() {
    int stanga_dreapta = 215;
    int inainte_inapoi = 115;
    char c;

    printf("%d\n", stanga_dreapta);
    printf("%d\n", inainte_inapoi);

    do {
        c = getchar();

        switch (c)
        {
            case 'w':
                if (inainte_inapoi != 120) {
                    ++inainte_inapoi;
                }
                printf("%d\n", inainte_inapoi);
                break;
            case 's':
                if (inainte_inapoi != 110) {
                    --inainte_inapoi;
                }
                printf("%d\n", inainte_inapoi);
                break;
            case 'a':
                if (stanga_dreapta != 210) {
                    --stanga_dreapta;
                }
                printf("%d\n", stanga_dreapta);
            case 'd':
                if (stanga_dreapta != 220) {
                    ++stanga_dreapta;
                }
                printf("%d\n", stanga_dreapta);
                break;
            case 'k':
                stanga_dreapta = 215;
                inainte_inapoi = 115;
                printf("%d\n", stanga_dreapta);
                printf("%d\n", inainte_inapoi);
        }
    } while (1);

    return 0;
}
