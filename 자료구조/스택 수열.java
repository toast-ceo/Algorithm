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
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringBuilder sb = new StringBuilder();
        //배열의 인덱스 값을 담당할 변수
        int index = 0;
        //1~n까지의 현재 값을 담당할 변수
        int num = 1;

        //입력값을 변수에 저장
        for(int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Stack<Integer> stack = new Stack<Integer>();

        //n개의 값으로 수열을 만들기때문에 index는 0부터 n-1까지이기때문에 n보다 작은경우에 반복한다.
        while(index < n) {
            //stack이 비어있지 않다는 조건문을 꼭 넣어준다. 당연하다 stack에 머가 있어야 pop을 할 수 있기때문에
            if(!stack.empty() && arr[index] < stack.get(stack.size() - 1)) {
                break;
            }else if(!stack.empty() && arr[index] == stack.get(stack.size() - 1)) {
                stack.pop();
                sb.append("-").append("\n");
                index++;
                //push해줄때는 stack이 비어있어도 된다.
            }else {
                while(num <= n) {
                    if(arr[index] != num) {
                        stack.push(num);
                        sb.append("+").append("\n");
                        num++;
                    }else {
                        stack.push(num);
                        sb.append("+").append("\n");
                        num++;
                        break;
                    }
                }
            }
        }

        if(index == n) {
            System.out.println(sb);
        }else {
            System.out.println("NO");
        }
    }
}
