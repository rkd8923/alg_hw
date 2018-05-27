package alg_hw3;
import java.util.Stack;
import java.util.ArrayList;
import java.util.Collections; 
import java.util.Comparator;

public class AdjacencyMatrix {
	int N;
	int[][] map;
	int[][] trans;
	ArrayList<Integer>[] scc_tree;
	
	@SuppressWarnings("unchecked")
	public AdjacencyMatrix(int n) { 
		this.N = n;
		this.map = new int[n+1][n+1];
		this.trans = new int[n+1][n+1];
		this.scc_tree = new ArrayList[n+1];
	}
	
	public void setInput(int x, int[] input) {
		for (int i=1; i<input.length; i++) { 
			if (input[i] != 0) this.map[x][input[i]] = 1;
		}

		for (int y=1; y<input.length; y++) {
			if (input[y] != 0) this.trans[input[y]][x] = 1;
		}
	}
	
	public int getElement(int x, int y) {
		return this.map[x][y];
	}
	public int getTrans(int x, int y) {
		return this.trans[x][y];
	}
	public int check_visit_end(int[] v) {
		for (int i=1; i<=this.N; i++) {
			if (v[i] == 0) { 
				return i;
			}
		}
		return 0;
	}
	public Stack<Integer> dfs() {
		Stack<Integer> finish = new Stack<>(); // Order of end vertex
		Stack<Integer> stack = new Stack<>();
		int[] visit = new int[this.N+1]; // visit[0] : unused, 1~N
		stack.push(1);  // DFS start
		visit[1] = 1;
		boolean flag; 
		while (!stack.isEmpty()) {
			flag = false;
			int vv = stack.peek();		
			for (int i=1; i<=this.N; i++) {
				if (this.map[vv][i] == 1 && visit[i] == 0) {
					stack.push(i);
					visit[i] = 1;
					flag = true;
					break;
				}
			}
			if (!flag) {
				finish.push(stack.pop());
				if (stack.isEmpty()) {
					int next = check_visit_end(visit);
					if (next != 0) {
						stack.push(next);
						visit[next] = 1;
					}
				}
			}	
		}
		
		return finish;
	}
	public ArrayList<Integer>[] scc() {
		Stack<Integer> order = this.dfs();
		Stack<Integer> stack = new Stack<>();		
		int[] visit = new int[this.N+1]; // visit[0] : unused, 1~N	
		ArrayList<Integer> scc_part = new ArrayList<>();
		stack.push(order.pop());
		visit[stack.peek()] = 1;
		scc_part.add(stack.peek());
		boolean flag; 
		while (!stack.isEmpty()) {
			flag = false;
			int vv = stack.peek();
			for (int i=1; i<=this.N; i++) {
				if (this.trans[vv][i] == 1 && visit[i] == 0) {
					stack.push(i);
					visit[i] = 1;
					scc_part.add(i);
					flag = true;
					break;
				}	
			}
			if (!flag) {
				stack.pop();
				if (stack.isEmpty()) {
					Collections.sort(scc_part);
					scc_tree[scc_part.get(0)] = scc_part;
					scc_part = new ArrayList<>();
					while (!order.isEmpty()) {
						int next = order.pop();
						if (visit[next] == 0) {
							stack.push(next);
							visit[next] = 1;
							scc_part.add(next);
							break;
						}
					}
				}
			}
		}
		
		return this.scc_tree;	
	}		
}
class AscendingInteger implements Comparator<Integer> {
	@Override
	public int compare(Integer a, Integer b) {
		return b.compareTo(a);
	}
}
