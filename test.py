def logic_skill():
    brain_score = 0
    practice_score = 0
    
    while True:
        brain_score += 1
        practice_score += 1
        
        print(f"\nProgress: Brain = {brain_score}, Practice = {practice_score}")
        if brain_score == 100 and practice_score == 100:
            print("🎉 Congratulations! Finally your hard work is paying off!")
            print("Practice makes perfect!!")
            break
            
        print("Keep going! The journey towards 100 continues....\n")
logic_skill()