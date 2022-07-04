#set operations

#1..union

#2..intersection

#3..difference

#1...union
#is the result of combination of 2 set
st={1,2,3,4,5,6,7,8,9,10}
st1={7,8,9,10,11,12,13,14,15}

#st union st1  ..{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}

st2=st.union(st1)
print(st2)

#2....intersection
#to collect the coman elements in the set

#st intersection st1  .{7,8,9,10}

st2=st.intersection(st1)
print(st2)

#3...difference
#a-b means elements present in set "a" but not present in set "b"

#st difference st1..{1,2,3,4,5,6}

st2=st.discard(st1)
print(st2)

#st1 difference st...{11,12,13,14,15}
st2=st1.discard(st)
print(st2)