abstract class Bank
{
	abstract int getROI();
	public void display()
	{
		System.out.println("RBI");
	}
}
class SBI extends Bank
{
	public int getROI()
	{
		return (6);
	}
}
class HDFC extends Bank
{
	public int getROI()
	{
		return (7);
	}
	public void show()
	{
		System.out.println("HDFC");
	}	
}
class AbstractDemo
{
	public static void main(String[] args)
	{
		Bank obj=null;
		obj=new SBI();
		System.out.println(obj.getROI());
		obj=new HDFC();
		System.out.println(obj.getROI());
	}
}