
�

room.protoroom	ddz.protomajiang.proto""
	REQ_ENTER

table_type (:0"E
	RSP_ENTER
result (:0
dest (:0
	table_gid (:0",
REQ_FRIEND_TABLE_INFO
password (:0"Q
RSP_FRIEND_TABLE_INFO
result (:0
dest (:0
	table_gid (:0"~
OneRecordResult
uid (:0
name (	: 
icon (	: 
count (:0
	win_times (:0
addscore (:0"2
RoundResult
uid (:0
addscore (:0"H
OneRoundInfo
round (:0&
result_list (2.room.RoundResult"�
FriendRecord
time (:0

table_type (:0
password (:0)

total_list (2.room.OneRecordResult'
detail_list (2.room.OneRoundInfo"(
REQ_FRECORD_LIST
	game_type (:0"e
RSP_FRECORD_LIST(
frecord_list (2.room.FriendRecord
result (:0
	game_type (:0".
REQ_FRIEND_TABLE_PANEL
	game_type (:0"�
FriendTableRow
password (:0

table_type (:0
icons (	

player_num (:0
zimo_addition (:0
total_count (:0"�
RSP_FRIEND_TABLE_PANEL
result (:0+
friend_tables (2.room.FriendTableRow
today_score (:0
	game_type (:0"/
PlayerScore
uid (:0
score (:0"�
FriendTable

create_uid (:0
password (:0

table_type (:0
	cur_count (:0
total_count (:0,
player_score_list (2.room.PlayerScore"�
REQ_CREATE_FRIEND_TABLE

table_type (:0-
ddz_create_conf (2.ddz.CreateTableConf0
xuezhan_create_conf (2.majiang.CreateConf"h
RSP_CREATE_FRIEND_TABLE
result (:0
dest (:0
	table_gid (:0
password (:0"B
NTF_FRIEND_TABLE_UPDATE'
update_table (2.room.FriendTable