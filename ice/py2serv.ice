#pragma once

module Demo
{

interface Hello
{
    void sayHello();
};

};

module Test 
{
	
	struct Message 
	{
		string date;
		int mission;
		string action;
		int idObjet;
	};
	sequence<Message> MessageList;
	interface Sender
	{
		void Send(Message msg);
	};
};
