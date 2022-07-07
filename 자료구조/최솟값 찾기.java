// 자료구조인 deque 개념에 대해 숙지 해야함.
// 슬라이드 윈도우 기법을 이용해서 풀어야함

// 간략한 예제 풀이 과정
//i=0 : [ {1,0} ]   ☛ bw.write : 1
//i=1 : [ {1,0}, {5,1} ] ☛ bw.write : 1 1
//i=2 : [ {1,0}, {5,1}, {2,2} ] ☛ bw.write : 1 1 1
//→ 새로 들어오는 값보다 이전의 값이 더 크다면 값을 빼준다. (5>2 :  q.peekLast()[0] > num)
//i=3 : [ {1,0}, {2,2}, {3,3} ] ☛ bw.write : 1 1 1 2
//→ 현재 최솟값의 인덱스가 창문의 너비 값을 벗어나면 삭제해준다. (0 < 1 : q.peek()[1] < i -(l-1))
//i=4 : [ {2,2}, {3,3}, {6,4} ] ☛ bw.write : 1 1 1 2 2
//i=5 : [ {2,2}, {3,3}, {6,4}, {2,5} ] ☛ bw.write : 1 1 1 2 2 2
//→ 새로 들어오는 값보다 이전의 값이 더 크다면 값을 빼준다. (3,6 > 2 : q.peekLast()[0] > num)
//→ 현재 최솟값의 인덱스가 창문의 너비 값을 벗어나면 삭제해준다. (2 < 3 : q.peek()[1] < i -(l-1))
//i=6 : [ {2,5}, {3,6} ] ☛ bw.write : 1 1 1 2 2 2 2
//i=7 : [ {2,5}, {3,6}, {7,7} ] ☛ bw.write : 1 1 1 2 2 2 2 2
//i=8 : [ {2,5}, {3,6}, {7,7}, {3,8} ] ☛ bw.write : 1 1 1 2 2 2 2 2 3
//→ 새로 들어오는 값보다 이전의 값이 더 크다면 값을 빼준다. (7 > 3 : q.peekLast()[0] > num)
//→ 현재 최솟값의 인덱스가 창문의 너비 값을 벗어나면 삭제해준다. (5 < 6 : q.peek()[1] < i -(l-1))
//i=9 : [ {3,6}, {3,8}, {5,9} ]  ☛ bw.write : 1 1 1 2 2 2 2 2 3 3
//i=10 : [ {3,6}, {3,8}, {5,9}, {2,10} ]  ☛ bw.write : 1 1 1 2 2 2 2 2 3 3 2
//→ 새로 들어오는 값보다 이전의 값이 더 크다면 값을 빼준다. (3,5 > 2 : q.peekLast()[0] > num)
//i=11 : [ {2,10}, {3,11} ]  ☛ bw.write : 1 1 1 2 2 2 2 2 3 3 2 2

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
