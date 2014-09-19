module Serv2client {
	struct Message {
		string date;
		int mission;
		string action;
		int idObjet;
	};
	sequence<Message> MessageList;
};