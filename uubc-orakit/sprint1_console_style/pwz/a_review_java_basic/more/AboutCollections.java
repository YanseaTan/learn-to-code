package pwz.a_review_java_basic.more;

import com.sun.jmx.remote.internal.ArrayQueue;

import java.util.*;

public class AboutCollections {

    /**
     * important but not urgent
     */
    public void aboutCollectionFramework(){
        // The Collection Interface:: !!Iterators
        // Generic Utility Methods
        // Interfaces in the Collections Framework:: !!Collection and Map
    }

    /**
     * @see java.util.AbstractCollection
     * list,set,queue
     */
    public static void tryCollections(){
        System.out.println("Try ArrayList =============================");
        ArrayList<Integer> intList = new ArrayList<>();
        intList.add(20);
        intList.add(16);
        intList.add(3);
        intList.add(56);
        // traverse the collection in plain way
        System.out.println("traverse the collection in plain way");
        for (int i=0; i< intList.size(); ++i){
            System.out.println(intList.get(i));
        }
        // using iterator to traverse the collection is more flexible and convenient
        System.out.println("using iterator to traverse the collection is more flexible and convenient");
        Iterator<Integer> intIt = intList.iterator();
        while (intIt.hasNext()){
            System.out.println(intIt.next());
        }
        // foreach syntax will call iterator automatically
        System.out.println("foreach syntax will call iterator automatically");
        for (int x : intList) {
            System.out.println(x);
        }

        // sort
        System.out.println("sort...");
        intList.sort((Integer i1, Integer i2)-> i1-i2);
        // intList.sort(Comparator.comparingInt((Integer i) -> i));
        for (int x: intList) System.out.println(x);

        System.out.println("Try HashSet =============================");
        // HashSet is an unordered collection that rejects duplicates
        HashSet<String> hashSet = new HashSet<>();
        System.out.println(hashSet.add("qwer")); //add return ture if set changed
        hashSet.add("wasd");
        hashSet.add("jklm");
        for (String s: hashSet) System.out.println(s);
        // reject duplicates
        System.out.println("hashSet reject duplicates");
        System.out.println(hashSet.add("qwer"));
        for (String s: hashSet) System.out.println(s);

        System.out.println("Try PriorityQueue =============================");
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(12);
        priorityQueue.add(123);
        priorityQueue.add(123);
        for (int x: priorityQueue) System.out.println(x);
        System.out.println("peek..." + priorityQueue.peek());
        for (int x: priorityQueue) System.out.println(x);
        System.out.println("poll..." + priorityQueue.poll());
        for (int x: priorityQueue) System.out.println(x);
    }

    /**
     * @see java.util.AbstractMap
     */
    public static void tryMaps(){
        // a hash map hashes the keys
        System.out.println("hash map...");
        HashMap<String, Integer> hashMap = new HashMap<>();
        hashMap.put("L", 19);
        hashMap.put("K", 36);
        hashMap.put("W", 21);
        for (String s: hashMap.keySet()) System.out.println(s + ": " + hashMap.get(s));
        System.out.println("remove K...");
        hashMap.remove("K");
        for (String s: hashMap.keySet()) System.out.println(s + ": " + hashMap.get(s));

        // a tree map uses an ordering on the keys to organize them in a search tree
        //  hashing is usually a bit faster, and it is the preferred choice
        //  if you don’t need to visit the keys in sorted order
        System.out.println("tree map...");
        TreeMap<String, Integer> treeMap = new TreeMap<>();
        treeMap.put("L", 19);
        treeMap.put("K", 36);
        treeMap.put("W", 21);
        for (String s: treeMap.keySet()) System.out.println(s + ": " + treeMap.get(s));
    }

    public static void main(String[] args) {
        tryCollections();
        tryMaps();
    }

    /**
     * what's more?
     */
    public void whatMore(){
        // 9.5 Views and Wrappers
        // 9.6 Algorithms
        // 9.7 Legacy Collections
    }
}
