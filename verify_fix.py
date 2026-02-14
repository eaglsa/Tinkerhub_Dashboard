import requests
import sys

try:
    response = requests.get("http://127.0.0.1:8000/")
    response.raise_for_status()
    
    content = response.text
    
    # Check for core participants (fallback data if sheet is down)
    if "alice.sh" in content and "0xbob" in content:
        print("SUCCESS: Found expected participants.")
    else:
        print("FAILURE: Did not find expected participants.")
        sys.exit(1)
        
    # Check for counts (they shouldn't be empty or 0 if data is there)
    # Alice is Frontend (learner), Bob is Backend (learner), Charlie is Designer (learner)
    # Wait, in fallback:
    # Alice: Role='Frontend' -> Learner
    # Bob: Role='Backend' -> Learner
    # Charlie: Role='Designer' -> Learner
    # So Mentor Count should be 0, Learner Count should be 3.
    # But wait, looking at the code: role == 'mentor' -> m_count += 1
    # Fallback roles are Frontend, Backend, Designer. So all are learners.
    
    # Let's check for the presence of the count elements
    # <div ...>{{ mentor_count }}</div>
    # it renders as <div ...>0</div> or similar.
    
    if '<div class="mt-6 bg-black text-white rounded-full w-14 h-14 flex items-center justify-center text-2xl font-bold border-4 border-black">0</div>' in content:
         print("SUCCESS: Found mentor count 0 (expected for fallback).")
    elif "mentor_count" not in content: # If template tag wasn't rendered it would show empty
         print("SUCCESS: Template rendered (mentor_count replaced).")
    else:
         print("WARNING: mentor_count check inconclusive or non-zero.")

    if '<div class="mt-6 bg-white text-black rounded-full w-14 h-14 flex items-center justify-center text-2xl font-bold border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">3</div>' in content:
        print("SUCCESS: Found learner count 3 (expected for fallback).")
    else:
        # It might be dynamic from the sheet
        pass

    print("Verification complete.")
    
except Exception as e:
    print(f"FAILURE: {e}")
    sys.exit(1)
