   43  git add .
   44  git commit -m "Ajustando arquivo .cs"
   45  git push
   46  kotlin
   47  pacman -Ss kotlin
   48  sudo pacman -S kotlin
   50  cd ..
   52  mkdir kotlin
   53  cd kotlin
   54  touch hello_world.kt
   55  curl -s https://get.sdkman.io | bash
   56  source "/home/manjaro/.sdkman/bin/sdkman-init.sh"
   57  sdk install kotlin
   59  kotlinc hello_world.kt -include-runtime -d hello_world.jar
   60  ls
   61  java -jar hello_world.jar
