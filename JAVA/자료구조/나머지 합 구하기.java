import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/*
 * 연속된 구간의 합이기 때문에 누적합 방법으로 문제를 풀이해야 한다.
 * 배열의 연속 구간의 합은 sum[j]−sum[i]로 구할 수 있는데, 이 합의 M으로 나눈 나머지가 0인 순서쌍을 구해야 한다.
 *
 * (sum[j]−sum[i]) % M = 0 이 되고, 모듈러 연산은 분배가 가능하기 때문에 sum[j] % M − sum[i] % M = 0
 * 따라서, sum[i] % M = sum[j] % M 인 개수를 구해주면 된다!
 *
 * 단, sum[i] % M = 0 인 경우에는 혼자만 존재해도 가능하기 때문에 이를 먼저 더해주어야 한다.
 * */

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int sum = 0;
        int[] count = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            sum = (sum + Integer.parseInt(st.nextToken())) % M;
            count[sum]++;
        }

        long ans = count[0];
        for (int i = 0; i < M; i++) {
            ans += (long) count[i] * (count[i] - 1) / 2;
        }
        System.out.println(ans);
    }
}