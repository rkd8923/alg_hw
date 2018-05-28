package alg_hw3;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;


public class AdjacencyArray {
	int N;
	int[][] array;
	int[][] trans;
	ArrayList<Integer>[] scc_tree;
	
	@SuppressWarnings("unchecked")
	public AdjacencyArray(int n) {
		this.N = n;
		this.array = new int[n+1][n+1];
		this.trans = new int[n+1][n+1];
		this.scc_tree = new ArrayList[n+1];
	}
	public void setInput(int n, int[] input) {
		for (int i=0; i<input.length; i++) {
			this.array[n][i] = input[i];
			if (i!=0) {
				int y = this.trans[input[i]][0] + 1;
				this.trans[input[i]][y] = n;
				this.trans[input[i]][0]++;
			}
		}
	}

	public int check_visit_end(int[] v) {
		for (int i=1; i<=this.N; i++) 
			if (v[i] == 0) return i;
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
			for (int i=1; i<=this.array[vv][0]; i++) {
				int y = this.array[vv][i];
				if (visit[y] == 0) {
					stack.push(y);
					visit[y] = 1;
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
			for (int i=1; i<=this.trans[vv][0]; i++) {
				int y = this.trans[vv][i];
				if (visit[y] == 0) {				
					stack.push(y);
					visit[y] = 1;
					scc_part.add(y);
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
