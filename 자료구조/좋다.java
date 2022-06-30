import java.io.IOException;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count = 0;
        int Num[] = new int[N];
        for (int i =0; i<N; i++){
            Num[i] = sc.nextInt();
        }
        Arrays.sort(Num);
        for (int k = 0; k<N; k++){
            long find = Num[k];
            int i =0;
            int j = N-1;
            while (i<j){
                if(Num[i]+ Num[j]== find){
                    if( i != k && j != k){
                        count++;
                        break;
                    }else if(i ==k){
                        i++;
                    }else if(j ==k){
                        j--;
                    }
                }else if(Num[i] + Num[j]< find){
                    i++;
                }else {
                    j--;
                }
            }
        }
        System.out.println(count);
    }
}
