import lichess.api
from lichess.format import SINGLE_PGN

# https://python-lichess.readthedocs.io/en/latest/


pgn = lichess.api.user_games('arvidj', max=200, format=SINGLE_PGN)

print(f'Fetched pgn: {pgn}')
with open('last200_arvidj.pgn', 'w', encoding='utf-8') as f:
   print(f'Writing pgn to file')
   f.write(pgn)