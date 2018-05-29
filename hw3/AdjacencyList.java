package alg_hw3;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

public class AdjacencyList {
	int N;
	ArrayList<ArrayList<Integer>> list;
	ArrayList<ArrayList<Integer>> trans; 
	ArrayList<Integer>[] scc_tree;
	
	@SuppressWarnings("unchecked")
	public AdjacencyList(int n) {
		N = n;
		this.list = new ArrayList<>(); 
		this.trans = new ArrayList<>();
		this.scc_tree = new ArrayList[n+1];
		
		
		ArrayList<Integer> dummy = new ArrayList<>();
		this.list.add(dummy);
		dummy = new ArrayList<>();
		this.trans.add(dummy);
		
		for (int i = 1; i <= n; i++) { 
			ArrayList<Integer> tmp = new ArrayList<>();
			this.list.add(tmp);
			tmp = new ArrayList<>();
			this.trans.add(tmp);
		}
	}
	public void setInput(int n, int[] input) {
		if (input[0] == 0) {
			this.list.get(n).add(0);
			return;
		}
		for (int i=1; i<input.length; i++) {
			this.list.get(n).add(input[i]);
			this.trans.get(input[i]).add(n);
		}
	}
	public ArrayList<Integer> getLine(int x) {
		return this.list.get(x);
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
			for (int i=0; i<this.list.get(vv).size(); i++) {
				int y = this.list.get(vv).get(i);
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
			for (int i=0; i<this.trans.get(vv).size(); i++) {
				int y = this.trans.get(vv).get(i);
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
