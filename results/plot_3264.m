
load("benchmark_64.mat")

subplot(3,2,1)
plot(d, gc, d, uc)
title("Ascon-p Cycles / bit vs. masking order (x86-64)")
xlabel("masking order")
ylabel("Cycles / bit")
legend("proposed (generic C)", "usuba compiled", "Location", 'northwest')

subplot(3,2,3)
plot(d, gr, d, ur)
title("Ascon-p Randomness usage vs. masking order (x86-64)")
xlabel("masking order")
ylabel("Random Bytes[byte]")
legend("proposed (generic C)", "usuba compiled", "Location", 'northwest')

load("codesize_64.mat")
subplot(3,2,5)
plot(d, gc, d, uc)
title("Ascon-p Codesize vs. masking order (x86-64)")
xlabel("masking order")
ylabel("Codesize [bytes]")
legend("proposed (generic C)", "usuba compiled", "Location", 'southeast')


load("benchmark_32.mat")

subplot(3,2,2)
plot(d, gc, d, uc)
title("Ascon-p Cycles / bit vs. masking order (x86)")
xlabel("masking order")
ylabel("Cycles / bit")
legend("proposed (generic C)", "usuba compiled", "Location", 'northwest')

subplot(3,2,4)
plot(d, gr, d, ur)
title("Ascon-p Randomness usage vs. masking order (x86)")
xlabel("masking order")
ylabel("Random bytes[byte]")
legend("proposed (generic C)", "usuba compiled", "Location", 'northwest')

load("codesize_32.mat")
subplot(3,2,6)
plot(d, gc, d, uc)
title("Ascon-p Codesize vs. masking order (x86)")
xlabel("masking order")
ylabel("Codesize [bytes]")
legend("proposed (generic C)", "usuba compiled", "Location", 'southeast')
