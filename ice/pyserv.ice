module pyserv {

	struct Message {
			string date;
			int mission;
			string action;
			int idObjet;
		};
	sequence<Message> MessageList;
	
	interface Sender{
		void send();
	};
			
};