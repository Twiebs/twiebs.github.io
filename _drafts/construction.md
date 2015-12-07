Some thoughts on construction

Let's examine current construction techinques in procedural and object oriented languages
currently in C++ this is how an object is typicaly constructed.  In this example i will be using a very basic MeshData struct from my game framework

struct Vertex3D { ... }; 

struct MeshData {
	uint32_t vertexCount;
	uint32_t indexCount;
	Vertex3D* vertices;
	uint32_t* indices;
};





