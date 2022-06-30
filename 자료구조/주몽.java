import java.io.IOException;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N =sc.nextInt();
        int sum = sc.nextInt();
        int Material[] = new int[N];

        for (int i =0; i< N ; i++){
            Material[i] = sc.nextInt();
        }
        Arrays.sort(Material);
        int i = 0;
        int j = N-1;
        int count = 0;
        while (i<j){
            if(Material[i]+Material[j] <sum){
                i++;
            }else if(Material[i]+Material[j]>sum){
                j--;
            }else {
                count++;
                i++;
                j--;
            }
        }
        System.out.println(count);
    }
}
