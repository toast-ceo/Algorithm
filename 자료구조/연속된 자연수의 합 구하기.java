import java.io.IOException;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N =sc.nextInt();
        sc.close();
        if(N<=2) {System.out.println(1);}
        else {
            int sum=0;
            int cnt=1;
            for (int i = 1; i <= N/2+1; i++) {
                sum=0;
                for (int j = i; sum <N; j++) {
                    sum+=j;
                    if(sum==N)cnt++;
                }
            }
            System.out.println(cnt);
        }
    }
}