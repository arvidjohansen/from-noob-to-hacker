from chessdotcom import get_player_profile, Client
   
Client.request_config["headers"]["User-Agent"] = (
    "My Python Application. "
    "Contact me at email@example.com"
)
response = get_player_profile("fabianocaruana")

player_name = response.json['player']['name']
#or
player_name = response.player.name