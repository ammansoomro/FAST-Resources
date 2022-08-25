package Task03;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.FileInputStream;
import java.util.Scanner;
public class Task3
{
	public static void main(String[] args) throws IOException {
		FileOutputStream out =	 new FileOutputStream("output.txt", false);
		Scanner input = new Scanner(System.in);
		String str1 = input.nextLine();
		input.close();
		byte[] b = str1.getBytes();
		out.write(b);
		out.close();
		FileInputStream in = new FileInputStream("output.txt");
		String str2 = "";
		int i = 0;
		while((i = in.read()) != -1)
			str2 += (char)i;
		System.out.println(str2);
	}
}