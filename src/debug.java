///백준
//문제 2 - 1546
//문제 3 - 11659
//문제 4 - 11660
//문제 5 - 10986
//문제 6 - 2018
//문제 7 - 1940
//문제 8 - 1253
//문제 9 - 12891
//문제 10 - 11003
//문제 11 - 1874
//문제 12 - 17298
//문제 13 - 2164
//문제 14 - 11286
//문제 15 - 2750
//문제 16 - 1377
//문제 17 - 1427
//문제 18 - 11399
//문제 19 - 11004
//문제 20 - 2751

// 슬라이드 윈도우
import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        Deque<int[]> q = new ArrayDeque<>();
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            int num = Integer.parseInt(st.nextToken());
            while(!q.isEmpty() && q.peekLast()[0] > num) q.pollLast();

            q.offer(new int[] {num,i});
            if(q.peek()[1] < i -(l-1)) {
                q.poll();
            }
            bw.write(q.peek()[0]+" ");
        }
        bw.flush();
        bw.close();
    }
}
