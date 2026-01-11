class MemoryUtilization {

    // Static data member (shared memory)
    static int count = 0;

    // Constructor
    MemoryUtilization() {
        count++;
    }

    // Static member function
    static void display() {

        System.out.println("\u001B[34m╔════════════════════════════════════╗\u001B[0m");
        System.out.println("\u001B[36m║   🌟 STATIC MEMORY UTILIZATION 🌟   ║\u001B[0m");
        System.out.println("\u001B[34m╠════════════════════════════════════╣\u001B[0m");

        System.out.println("\u001B[33m║ Total Objects Created : \u001B[32m" + count + "         \u001B[33m║\u001B[0m");

        System.out.println("\u001B[34m╠════════════════════════════════════╣\u001B[0m");

        System.out.println("\u001B[32m║ ✔ ONE static variable in memory    ║\u001B[0m");
        System.out.println("\u001B[32m║ ✔ Memory shared by all objects     ║\u001B[0m");
        System.out.println("\u001B[32m║ ✔ Efficient memory utilization    ║\u001B[0m");

        System.out.println("\u001B[34m╚════════════════════════════════════╝\u001B[0m");
    }
}

public class StaticDemo {
    public static void main(String[] args) {

        // Creating multiple objects
        new MemoryUtilization();
        new MemoryUtilization();
        new MemoryUtilization();
        new MemoryUtilization();

        // Calling static method
        MemoryUtilization.display();
    }
}
