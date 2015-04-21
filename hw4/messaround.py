fo = open("/home/andrew/sp2015.11-731/hw4/data/sample.input")
sample = fo.readlines()
fo2 = open("/home/andrew/sp2015.11-731/hw4/data/sample.refs")
refs = fo2.readlines()

phrases = []
prev_ft_strings = []
Next_ft_strings = []
input_line_index = -1

for line in sample:
    input_line_index += 1
    left_context, phrase, right_context = [part.strip() for part in line.decode('utf-8').strip().split('|||')]
    left_context = left_context.strip().split()
    right_context = right_context.strip().split()
    #print "line = ", line.strip()
    if len(left_context) > 0:
        prev = left_context[-1]
    else:
        prev = "<s>"
    if len(right_context) > 0:
        Next = right_context[0]
    else:
        Next = "</s>"

    correct_czech = refs[input_line_index].decode("UTF-8").strip()
    prev_ft_str = "src:" + phrase + "_tgt:" + correct_czech + "_prev:" + prev
    next_ft_str = "src:" + phrase + "_tgt:" + correct_czech + "_next:" + Next
    #print "prev_ft_str = ", prev_ft_str
    #print "next_ft_str = ", next_ft_str
    prev_ft_strings.append(prev_ft_str)
    Next_ft_strings.append(next_ft_str)
    phrases.append(phrase)
    #print "\n"
phrases_set = sorted(set(phrases))
prev_ft_strings_set = sorted(set(prev_ft_strings))
Next_ft_strings_set = sorted(set(Next_ft_strings))
print "len prev set = ", len(prev_ft_strings_set)
print "len Next set = ", len(Next_ft_strings_set)
print "prev_ft_strings_set = ", prev_ft_strings_set
print "Next_ft_strings_set = ", Next_ft_strings_set
