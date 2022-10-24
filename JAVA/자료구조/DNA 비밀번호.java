
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 슬라이딩 윈도우 기법을 이용해야함
class Main {

    static int answer;
    static String str;
    static Map<Character, Integer> require;

    public static void main(String[] args) throws IOException {

        answer = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int entire = Integer.parseInt(st.nextToken());
        int part = Integer.parseInt(st.nextToken());
        str = br.readLine();

        require = new HashMap<>();
        st = new StringTokenizer(br.readLine());
        require.put('A', -Integer.parseInt(st.nextToken()));
        require.put('C', -Integer.parseInt(st.nextToken()));
        require.put('G', -Integer.parseInt(st.nextToken()));
        require.put('T', -Integer.parseInt(st.nextToken()));

        addInRange(0, part);

        int left = 0;
        int right = part;
        while (true) {
            check();
            if (right >= entire) {
                break;
            }
            removeInRange(left, left + 1);
            addInRange(right, right + 1);
            left++;
            right++;
        }

        System.out.println(answer);
    }

    private static void check() {
        for (Integer value : require.values()) {
            if (value < 0) {
                return;
            }
        }
        answer++;
    }

    private static void addInRange(int start, int end) {
        for (int i = start; i < end; i++) {
            require.compute(str.charAt(i), (character, integer) -> integer + 1);
        }
    }

    private static void removeInRange(int start, int end) {
        for (int i = start; i < end; i++) {
            require.compute(str.charAt(i), (character, integer) -> integer - 1);
        }
    }

}

