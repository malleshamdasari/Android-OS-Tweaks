int main(void) {
#pragma omp parallel
  {
    volatile unsigned x=0, y=1;
    while (x++ || y++);
  }
  return 0;
}
