std: :pair < int, int > new_coordonates = {state.first, state.second};
int
h = -1;

auto
leftMovements = [ &]()
{
if (checkPoints(parking, state.first, state.second - 1))
{
if (h == -1)
{
    h = getPotentialH(state.first, state.second - 1);
new_coordonates = std : :make_pair(state.first, state.second - 1);
}
else if (h > getPotentialH(state.first, state.second - 1)) {
h = getPotentialH(state.first, state.second - 1);
new_coordonates = std ::
    make_pair(state.first, state.second - 1);
}
}
else if (checkPoints(parking, state.first, state.second - 2)) {
if (h == -1) {
h = getPotentialH(state.first, state.second - 2);
new_coordonates = std ::
    make_pair(state.first, state.second - 2);
}
else if (h > getPotentialH(state.first, state.second - 2)) {
h = getPotentialH(state.first, state.second - 2);
new_coordonates = std ::
    make_pair(state.first, state.second - 2);
}
}
};
auto
rightMovements = [ &]()
{
if (checkPoints(parking, state.first, state.second + 1))
{
if (h == -1)
{
    h = getPotentialH(state.first, state.second + 1);
new_coordonates = std : :make_pair(state.first, state.second + 1);
}
else if (h > getPotentialH(state.first, state.second + 1)) {
h = getPotentialH(state.first, state.second + 1);
new_coordonates = std ::
    make_pair(state.first, state.second + 1);
}
}
else if (checkPoints(parking, state.first, state.second + 2)) {
if (h == -1) {
h = getPotentialH(state.first, state.second + 2);
new_coordonates = std ::
    make_pair(state.first, state.second + 2);
}
else if (h > getPotentialH(state.first, state.second + 2)) {
h = getPotentialH(state.first, state.second + 2);
new_coordonates = std ::
    make_pair(state.first, state.second + 2);
}
}
};
auto
upMovements = [ &]()
{
if (checkPoints(parking, state.first - 1, state.second))
{
if (h == -1)
{
    h = getPotentialH(state.first - 1, state.second);
new_coordonates = std : :make_pair(state.first - 1, state.second);
}
else if (h > getPotentialH(state.first - 1, state.second)) {
h = getPotentialH(state.first - 1, state.second);
new_coordonates = std ::
    make_pair(state.first - 1, state.second);
}
}
else if (checkPoints(parking, state.first - 2, state.second)) {
if (h == -1) {
h = getPotentialH(state.first - 2, state.second);
new_coordonates = std ::
    make_pair(state.first - 2, state.second);
}
else if (h > getPotentialH(state.first - 2, state.second)) {
h = getPotentialH(state.first - 2, state.second);
new_coordonates = std ::
    make_pair(state.first - 2, state.second);
}
}
};
auto
downMovements = [ &]()
{
if (checkPoints(parking, state.first + 1, state.second))
{
if (h == -1)
{
    h = getPotentialH(state.first + 1, state.second);
new_coordonates = std : :make_pair(state.first + 1, state.second);
}
else if (h > getPotentialH(state.first + 1, state.second)) {
h = getPotentialH(state.first + 1, state.second);
new_coordonates = std ::
    make_pair(state.first + 1, state.second);
}
}
else if (checkPoints(parking, state.first + 2, state.second)) {
if (h == -1) {
h = getPotentialH(state.first + 2, state.second);
new_coordonates = std ::
    make_pair(state.first + 2, state.second);
}
else if (h > getPotentialH(state.first + 2, state.second)) {
h = getPotentialH(state.first + 2, state.second);
new_coordonates = std ::
    make_pair(state.first + 2, state.second);
}
}
};

upMovements();
downMovements();
leftMovements();
rightMovements();
std: :pair < int, int > new_coordonates = {state.first, state.second};
int
h = -1;

auto
leftMovements = [ &]()
{
if (checkPoints(parking, state.first, state.second - 1))
{
if (h == -1)
{
    h = getPotentialH(state.first, state.second - 1);
new_coordonates = std : :make_pair(state.first, state.second - 1);
}
else if (h > getPotentialH(state.first, state.second - 1)) {
h = getPotentialH(state.first, state.second - 1);
new_coordonates = std ::
    make_pair(state.first, state.second - 1);
}
}
else if (checkPoints(parking, state.first, state.second - 2)) {
if (h == -1) {
h = getPotentialH(state.first, state.second - 2);
new_coordonates = std ::
    make_pair(state.first, state.second - 2);
}
else if (h > getPotentialH(state.first, state.second - 2)) {
h = getPotentialH(state.first, state.second - 2);
new_coordonates = std ::
    make_pair(state.first, state.second - 2);
}
}
};
auto
rightMovements = [ &]()
{
if (checkPoints(parking, state.first, state.second + 1))
{
if (h == -1)
{
    h = getPotentialH(state.first, state.second + 1);
new_coordonates = std : :make_pair(state.first, state.second + 1);
}
else if (h > getPotentialH(state.first, state.second + 1)) {
h = getPotentialH(state.first, state.second + 1);
new_coordonates = std ::
    make_pair(state.first, state.second + 1);
}
}
else if (checkPoints(parking, state.first, state.second + 2)) {
if (h == -1) {
h = getPotentialH(state.first, state.second + 2);
new_coordonates = std ::
    make_pair(state.first, state.second + 2);
}
else if (h > getPotentialH(state.first, state.second + 2)) {
h = getPotentialH(state.first, state.second + 2);
new_coordonates = std ::
    make_pair(state.first, state.second + 2);
}
}
};
auto
upMovements = [ &]()
{
if (checkPoints(parking, state.first - 1, state.second))
{
if (h == -1)
{
    h = getPotentialH(state.first - 1, state.second);
new_coordonates = std : :make_pair(state.first - 1, state.second);
}
else if (h > getPotentialH(state.first - 1, state.second)) {
h = getPotentialH(state.first - 1, state.second);
new_coordonates = std ::
    make_pair(state.first - 1, state.second);
}
}
else if (checkPoints(parking, state.first - 2, state.second)) {
if (h == -1) {
h = getPotentialH(state.first - 2, state.second);
new_coordonates = std ::
    make_pair(state.first - 2, state.second);
}
else if (h > getPotentialH(state.first - 2, state.second)) {
h = getPotentialH(state.first - 2, state.second);
new_coordonates = std ::
    make_pair(state.first - 2, state.second);
}
}
};
auto
downMovements = [ &]()
{
if (checkPoints(parking, state.first + 1, state.second))
{
if (h == -1)
{
    h = getPotentialH(state.first + 1, state.second);
new_coordonates = std : :make_pair(state.first + 1, state.second);
}
else if (h > getPotentialH(state.first + 1, state.second)) {
h = getPotentialH(state.first + 1, state.second);
new_coordonates = std ::
    make_pair(state.first + 1, state.second);
}
}
else if (checkPoints(parking, state.first + 2, state.second)) {
if (h == -1) {
h = getPotentialH(state.first + 2, state.second);
new_coordonates = std ::
    make_pair(state.first + 2, state.second);
}
else if (h > getPotentialH(state.first + 2, state.second)) {
h = getPotentialH(state.first + 2, state.second);
new_coordonates = std ::
    make_pair(state.first + 2, state.second);
}
}
};

upMovements();
downMovements();
leftMovements();
rightMovements();

if (h != -1) {
move(parking, new_coordonates.first, new_coordonates.second);
}
if (h != -1) {
move(parking, new_coordonates.first, new_coordonates.second);
}

upMovements()
downMovements()
leftMovements()
rightMovements()

if(h!=-1):
    move(parking, new_coordonates.first, new_coordonates.second)

if(h!=-1):
    move(parking, new_coordonates.first, new_coordonates.second)