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

        Scanner in = new Scanner(System.in);
        Stack<Integer> stack = new Stack<Integer>();

        int N = in.nextInt();
        int[] seq = new int[N];

        for(int i = 0; i < N; i++) {
            seq[i] = in.nextInt();
        }
        for(int i = 0; i < N; i++) {

            /*
             * 스택이 비어있지 않으면서
             * 현재 원소가 스택의 맨 위 원소가 가리키는 원소보다 큰 경우
             * 해당 조건을 만족할 때 까지 stack의 원소를 pop하면서
             * 해당 인덱스의 값을 현재 원소로 바꿔준다.
             */
            while(!stack.isEmpty() && seq[stack.peek()] < seq[i]) {
                seq[stack.pop()] = seq[i];
            }

            stack.push(i);
        }
        /*
         * 스택의 모든 원소를 pop하면서 해당 인덱스의 value를
         * -1로 초기화한다.
         */
        while(!stack.isEmpty()) {
            seq[stack.pop()] = -1;
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < N; i++) {
            sb.append(seq[i]).append(' ');
        }

        System.out.println(sb);
    }
}
