cd ../game/
rm -rf input
mkdir input
python generate.py
cd ../hadoop/
rm -rf input
mv ../game/input .
./command.sh
cp output/part-00000 ../workplace/learned.qvalues
rm -rf output
cd ../game
python test_qlearn.py ../workplace/learned.qvalues > ../workplace/learn_result.txt
cd ../workplace
cat learn_result.txt
