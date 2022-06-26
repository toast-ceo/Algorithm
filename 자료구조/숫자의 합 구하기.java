import java.util.Scanner;

class Main {
    public static void main(String[] arg){
       Scanner in = new Scanner(System.in);

       int Num = in.nextInt();
       String str = in.next();
       in.close();

       int sum = 0;

       for(int a = 0; a< Num; a++){
           sum += str.charAt(a) - '0';
       }
        System.out.println(sum);
    }
}