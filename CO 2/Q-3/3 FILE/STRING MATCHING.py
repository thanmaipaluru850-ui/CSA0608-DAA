START
INPUT text T
INPUT pattern P

n = length(T)
m = length(P)
comparisons = 0
positions = empty list

FOR i = 0 TO n-m
    j = 0

    WHILE j < m
        comparisons = comparisons + 1

        IF T[i+j] != P[j]
            BREAK
        END IF

        j = j + 1
    END WHILE

    IF j == m
        ADD i TO positions
    END IF
END FOR

PRINT positions
PRINT comparisons
STOP
