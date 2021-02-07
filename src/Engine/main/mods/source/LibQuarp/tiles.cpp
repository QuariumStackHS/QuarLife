#include "mods/LibQuarp/tiles/tiles.h"
//#include "pqxx/"
Tile::Tile(){

}
int TileRegisterer::registertile(Tile T)
{
    this->Tiles[NextID]=T;
}

int TileRegisterer::RegisterTiles()
{
    this->registertile(Tile().);
}