is_completed = True
sub_total = 25
tip_a = sub_total * .10
tip_b = sub_total * .20
tip_c = sub_total * .30

total = sub_total + tip_c
if total > tip_a or total > tip_b:
print('Thank you! Your total is ' + '$' + str(total))
if total > tip_c:
print('You are awesome!')
