#include<stdio.h>
#include<stdlib.h>
#include<Windows.h>
#include<iostream>
void click(int x,int y)
{

 SetCursorPos(x,y);
 mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0,0);
 mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0); 
}

int main()
{
	int y=117;
	system("C://Users//Eric//AppData//Local//LINE//bin//LineLauncher.exe");
	Sleep(1000);
	for(int j=0;j<3;j++)
	{
		int count=10;
		if(j==0)
			y=109;
		else if(j==1)
		{
			y=89;
			count=11;	
		} 
		else 
			y=137;
		for(int i=0;i<count;i++)
		{
			click(210,y);	//點群組 
		 	Sleep(500);
		 	click(1522,56);	//點選項 
		 	Sleep(500);
		 	click(1467,269);	//點儲存 
		 	Sleep(500);
			keybd_event(VK_RETURN,0,0,0);
			y+=72.5;		
		}
		click(368,809);
		Sleep(500); 
	}
	system("pause");
}
