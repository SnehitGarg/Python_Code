import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        
            try{
                final int PORT=12345;
                
                ServerSocket sskt = new ServerSocket(PORT);
                System.out.println("My Server Start Successfully");
                System.out.println("Port num"+sskt.getLocalPort());
                System.out.println("Waiting for client connetion...");
                //sskt.setSoTimeout(5000);
                Socket skt=sskt.accept();

                System.out.println("Client is connected:"+skt);

                BufferedReader in =new BufferedReader(new InputStreamReader(skt.getInputStream()));
                BufferedReader keyboard=new BufferedReader(new InputStreamReader(System.in));
                PrintWriter out=new PrintWriter(skt.getOutputStream(),true);
                String str= null;
                do{
                    str=in.readLine();
                    System.out.println("from client"+str);
                    str=keyboard.readLine();
                    out.println(str);
                }

                while(!str.equalsIgnoreCase("quit"));
                
            }
            catch(Exception e)
            {
                System.out.println(e);
            }
        
    }
    
}