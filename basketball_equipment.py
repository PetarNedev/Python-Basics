year_rate=int(input())
shoes=year_rate-(year_rate*(40/100))
dress=shoes-(shoes*(20/100))
ball=dress-(dress*(75/100))
accessories=ball-(ball*(80/100))
expenses=year_rate+shoes+dress+ball+accessories
print(expenses)
