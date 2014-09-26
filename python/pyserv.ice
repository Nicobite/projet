module pyserv {

	struct Message {
			string date;
			int mission;
			string action;
			int idObjet;
	};
	
	interface Sender{
		void send(int round);
		void shutdown();
	};
			
};