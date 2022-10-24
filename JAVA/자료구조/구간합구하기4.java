import java.util.*;

class Main {
    public static void main(String[] arg){
        Scanner in = new Scanner(System.in);

        // 입력 갯수
        int N = in.nextInt();
        // 출력 갯수
        int M = in.nextInt();
        int[] arr = new int[N+1];

        // 합한 값을 배열에 저장
        for(int i = 1; i<= N; i++) {
            int x = in.nextInt();
            arr[i] = arr[i-1]+x;
        }

        // 구간을 계산해서 출력해주는 부분
        for(int i = 0; i<M; i++) {
            int x = in.nextInt();
            int y = in.nextInt();

            System.out.println(arr[y]-arr[x-1]);

        }
    }
}