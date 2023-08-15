import java.util.LinkedList;

class hello{
    public static void main(String[] args) {
        System.out.println("hello");
        LinkedList<String> ll=new LinkedList<>();
        ll.add("a");
        ll.add("b");
        ll.add("c");
        System.out.println(ll);
        ll.addFirst("e");
        ll.addLast("d");
        ll.remove(3);
        ll.remove("c");
        System.out.println(ll);
       


    }
}